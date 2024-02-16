package core

import (
	"context"
	"encoding/json"
	"log/slog"
	"os"

	"shishifubing.com/leetcode/model"
)

type SubmissionsRepo struct {
	config  *model.Config
	storage *model.SubmissonsStorage
	ctx     context.Context
	logger  *slog.Logger
}

func NewSubmissionsRepo(config *model.Config, ctx context.Context, logger *slog.Logger) (*SubmissionsRepo, error) {
	repo := &SubmissionsRepo{
		config: config, storage: &model.SubmissonsStorage{}, ctx: ctx, logger: logger,
	}
	err := repo.readStorageFile()
	if err != nil {
		return nil, err
	}
	return repo, nil
}

func (r *SubmissionsRepo) AddSubmissions(submissions []*model.Submission) {
	curSubmissions := r.storage.Submissions
	for _, submission := range submissions {
		if _, ok := curSubmissions[submission.Id]; !ok {
			curSubmissions[submission.Id] = submission
		}
	}
}

func (r *SubmissionsRepo) readStorageFile() error {
	body, err := os.ReadFile(r.config.SubmissionsFile)
	if err != nil {
		return err
	}
	return json.Unmarshal(body, r.storage)
}

func (r *SubmissionsRepo) writeStorageFile() error {
	text, err := json.Marshal(r.storage)
	if err != nil {
		return err
	}
	return os.WriteFile(r.config.SubmissionsFile, text, 0644)
}
