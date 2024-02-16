package cmd

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

	"shishifubing.com/leetcode/core"
	"shishifubing.com/leetcode/model"
)

func Run(
	ctx context.Context,
	args []string,
	getenv func(string) string,
	stdin io.Reader,
	stdout, stderr io.Writer,
) error {
	logger := slog.New(slog.NewTextHandler(stderr, &slog.HandlerOptions{AddSource: true}))
	ctx, cancel := signal.NotifyContext(ctx, os.Interrupt)
	defer cancel()
	config, err := parseArgs(args, getenv)
	if err != nil {
		return err
	}
	_, err = core.NewSubmissionsRepo(config, ctx, logger)
	if err != nil {
		return err
	}
	downloader, err := core.NewSubmissionsDownloader(config, ctx, logger)
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
		stdout.Write(text)
	}
	return err
}

func parseArgs(args []string, getenv func(string) string) (*model.Config, error) {
	config := &model.Config{}
	const sessionReplace = "${LEETCODE_SESSION}"
	flagset := flag.NewFlagSet("flags", flag.ContinueOnError)
	flagset.StringVar(&config.BaseUrl, "base_url", model.ConfigDefault.BaseUrl, "")
	flagset.StringVar(&config.Session, "session", sessionReplace, "")
	flagset.StringVar(&config.SubmissionsFile, "submissions-file", model.ConfigDefault.SubmissionsFile, "")
	flagset.StringVar(&config.SubmissionsFile, "submissions-dir", model.ConfigDefault.SubmissionsDir, "")
	flagset.Uint64Var(&config.Offset, "offset", model.ConfigDefault.Offset, "")
	flagset.Uint64Var(&config.Limit, "limit", model.ConfigDefault.Limit, "")
	err := flagset.Parse(args)
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
