package core

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"log/slog"
	"os"
	"path/filepath"

	"shishifubing.com/leetcode/model"
)

type Generator struct {
	config *model.Config
	ctx    context.Context
	logger *slog.Logger
}

var extensions = map[string]string{"python3": "py", "golang": "go", "cpp": "cpp", "java": "java"}

func NewGenerator(config *model.Config, ctx context.Context, logger *slog.Logger) (*Generator, error) {
	generator := &Generator{
		config: config,
		ctx:    ctx,
		logger: logger,
	}
	return generator, nil
}

func (g *Generator) Generate(submissions []*model.Submission) error {
	count := 0
	for _, submission := range submissions {
		if submission.StatusDisplay != "Accepted" {
			continue
		}
		if err := g.write(submission); err != nil {
			return err
		}
		count += 1
	}
	g.logger.Info(fmt.Sprintf("wrote %d submissions to %s", count, g.config.SubmissionsDir))
	return nil
}

func (g *Generator) write(submission *model.Submission) error {
	name, err := g.submissionName(submission)
	if err != nil {
		return err
	}
	content, err := g.submissionContent(submission)
	if err != nil {
		return err
	}
	filePath := filepath.Join(g.config.SubmissionsDir, name)
	err = os.WriteFile(filePath, content, 0644)
	if err != nil {
		return fmt.Errorf("could not write '%s': %w", filePath, err)
	}
	return nil
}

func (g *Generator) submissionName(submission *model.Submission) (string, error) {
	extension, ok := g.config.Extensions[submission.Lang]
	if !ok {
		return "", fmt.Errorf("no extension for lang '%s'", submission.Lang)
	}
	name := fmt.Sprintf("%05d-%d-%s.%s", submission.QuestionId, submission.Id, submission.TitleSlug, extension)
	return name, nil
}

func (g *Generator) submissionContent(submission *model.Submission) ([]byte, error) {
	templ, err := model.SubmissionTemplate()
	if err != nil {
		return nil, err
	}
	var buffer bytes.Buffer
	err = templ.Execute(io.Writer(&buffer), map[string]any{
		"Config":     g.config,
		"Submission": submission,
	})
	if err != nil {
		return nil, fmt.Errorf("could not parse submission template: %w", err)
	}
	return buffer.Bytes(), nil
}
