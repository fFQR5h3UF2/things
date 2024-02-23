package leetcode

import (
	"context"
	"encoding/json"
	"fmt"
	"log/slog"
	"os"

	"shishifubing.com/pkg/leetcode/model"
)

type Repo struct {
	config *model.Config
	ctx    context.Context
	logger *slog.Logger
}

func NewRepo(config *model.Config, ctx context.Context, logger *slog.Logger) *Repo {
	return &Repo{config: config, ctx: ctx, logger: logger}
}

func (r *Repo) Submissions() ([]*model.Submission, error) {
	submissions, err := r.readStorageFile()
	if err != nil {
		return nil, err
	}
	return submissions.Submissions, nil
}

func (r *Repo) AddSubmissions(submissions []*model.Submission) error {
	curSubmissions, err := r.readStorageFile()
	if err != nil {
		return err
	}
	r.addSubmissions(curSubmissions, submissions)
	return r.writeStorageFile(curSubmissions)
}

func (r *Repo) addSubmissions(curSubmissions *model.SubmissonsStorage, newSubmissions []*model.Submission) {
	ids := map[uint64]struct{}{}
	for _, submission := range curSubmissions.Submissions {
		ids[submission.Id] = struct{}{}
	}
	countNew := 0
	for _, submission := range newSubmissions {
		if _, ok := ids[submission.Id]; !ok {
			countNew += 1
			curSubmissions.Submissions = append(curSubmissions.Submissions, submission)
		}
	}
	r.logger.Info(fmt.Sprintf("added %d submissions", countNew))
}

func (r *Repo) readStorageFile() (*model.SubmissonsStorage, error) {
	body, err := os.ReadFile(r.config.SubmissionsFile)
	if err != nil {
		return nil, fmt.Errorf("could not read '%s': %w", r.config.SubmissionsFile, err)
	}
	storage := &model.SubmissonsStorage{}
	err = json.Unmarshal(body, storage)
	if err != nil {
		return nil, fmt.Errorf("could not parse '%s': %w", r.config.SubmissionsFile, err)
	}
	return storage, nil
}

func (r *Repo) writeStorageFile(storage *model.SubmissonsStorage) error {
	text, err := json.MarshalIndent(storage, "", "  ")
	if err != nil {
		return fmt.Errorf("could not write '%s': %w", r.config.SubmissionsFile, err)
	}
	text = append(text, '\n')
	err = os.WriteFile(r.config.SubmissionsFile, text, 0644)
	if err != nil {
		return fmt.Errorf("could not write '%s': %w", r.config.SubmissionsFile, err)
	}
	r.logger.Info(fmt.Sprintf("wrote %d submissions to '%s'", len(storage.Submissions), r.config.SubmissionsFile))
	return nil
}
