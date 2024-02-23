package leetcode

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log/slog"
	"os"
	"os/signal"
	"strings"

	"shishifubing.com/pkg/leetcode/model"
)

func Run(
	ctx context.Context,
	args []string,
	getenv func(string) string,
	stdin io.Reader,
	stdout, stderr io.Writer,
) error {
	logger := slog.New(slog.NewTextHandler(stderr, &slog.HandlerOptions{}))
	ctx, cancel := signal.NotifyContext(ctx, os.Interrupt)
	defer cancel()
	config, err := parseArgs(args, getenv)
	if err != nil {
		return err
	}
	repo := NewRepo(config, ctx, logger)
	if err != nil {
		return err
	}
	downloader, err := NewDownloader(config, ctx, logger)
	if err != nil {
		return err
	}
	generator, err := NewGenerator(config, ctx, logger)
	if err != nil {
		return err
	}
	switch config.Action {
	case model.CliAction_DOWNLOAD:
		submissions, err := downloader.GetSubmissions(config.Offset, config.Limit)
		if err != nil {
			return err
		}
		text, err := json.Marshal(submissions)
		if err != nil {
			return err
		}
		text = append(text, '\n')
		stdout.Write(text)
	case model.CliAction_UPDATE:
		submissions, err := downloader.GetSubmissions(config.Offset, config.Limit)
		if err != nil {
			return err
		}
		return repo.AddSubmissions(submissions)
	case model.CliAction_GENERATE:
		submissions, err := repo.Submissions()
		if err != nil {
			return err
		}
		err = generator.Generate(submissions)
		if err != nil {
			return err
		}
	default:
		return fmt.Errorf("unsupported action: %s", config.Action)
	}
	return nil
}

func parseArgs(args []string, getenv func(string) string) (*model.Config, error) {
	configDefault, err := model.DefaultConfig()
	if err != nil {
		return nil, err
	}
	config := &model.Config{
		Extensions: configDefault.Extensions,
		Headers:    configDefault.Headers,
		Comments:   configDefault.Comments,
	}
	const sessionReplace = "${LEETCODE_SESSION}"
	flagset := flag.NewFlagSet("flags", flag.ContinueOnError)
	flagset.StringVar(&config.BaseUrl, "base_url", configDefault.BaseUrl, "")
	flagset.StringVar(&config.Session, "session", sessionReplace, "")
	flagset.StringVar(&config.SubmissionsFile, "submissions-file", configDefault.SubmissionsFile, "")
	flagset.StringVar(&config.SubmissionsDir, "submissions-dir", configDefault.SubmissionsDir, "")
	flagset.Uint64Var(&config.Offset, "offset", configDefault.Offset, "")
	flagset.Uint64Var(&config.Limit, "limit", configDefault.Limit, "")
	err = flagset.Parse(args)
	if err != nil {
		return nil, err
	}
	if config.Session == sessionReplace {
		config.Session = getenv("LEETCODE_SESSION")
	}
	action := flagset.Args()
	if len(action) == 0 {
		config.Action = model.CliAction_DOWNLOAD
	} else if len(action) == 1 {
		actionName := action[0]
		val, ok := model.CliAction_value[strings.ToUpper(actionName)]
		if !ok {
			return nil, fmt.Errorf("invalid action %s", actionName)
		}
		config.Action = model.CliAction(val)
	} else {
		return nil, fmt.Errorf("too many positional arguments")
	}
	return config, nil
}
