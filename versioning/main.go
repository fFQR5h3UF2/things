package main

import (
	"fmt"
	"log/slog"
	"os"
	"time"

	"github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing"
	"github.com/go-git/go-git/v5/plumbing/object"
	"golang.org/x/mod/semver"
)

func main() {
	stderr := os.Stderr
	logger := slog.New(slog.NewTextHandler(stderr, &slog.HandlerOptions{}))
	svc := &service{logger: logger}
	ver, err := svc.CurrentVersion()
	if err != nil {
		logger.Error(err.Error())
		os.Exit(1)
	}
	fmt.Println(ver)
}

type service struct {
	logger *slog.Logger
}

func (s *service) FilterTags(repo *git.Repository, filter func(tag *object.Tag) (bool, error)) ([]*object.Tag, error) {
	tags, err := repo.Tags()
	if err != nil {
		return nil, fmt.Errorf("could not get tags: %w", tags)
	}
	res := []*object.Tag{}
	err = tags.ForEach(func(ref *plumbing.Reference) error {
		hash := ref.Hash()
		obj, err := repo.TagObject(hash)
		switch err {
		case nil:
			ok, err := filter(obj)
			if err != nil {
				return fmt.Errorf("error during filtering %s: %w", obj.Name, err)
			}
			if ok {
				res = append(res, obj)
			}
			s.logger.Debug(fmt.Sprintf("result of filtering %s: %v", obj.Name, ok))
			return nil
		case plumbing.ErrObjectNotFound:
			s.logger.Debug(fmt.Sprintf("not a tag object: %s", ref))
			return nil
		default:
			return fmt.Errorf("unexpected error during tag parsing: %w", err)
		}
	})
	if err != nil {
		return nil, fmt.Errorf("could not filter tags: %w", err)
	}
	return res, nil
}

func (s *service) NewVersion() (string, error) {
	now := time.Now()
	year, week := now.ISOWeek()
	return fmt.Sprintf("%s.%s.0", year, week), nil
}

func (s *service) CurrentVersion() (string, error) {
	repo, err := git.PlainOpen(".")
	if err != nil {
		return "", err
	}
	filter := func(tag *object.Tag) (bool, error) { return semver.IsValid(tag.Name), nil }
	tags, err := s.FilterTags(repo, filter)
	if err != nil {
		return "", err
	}
	length := len(tags)
	if length == 0 {
		return s.NewVersion()
	}
	tagNames := make([]string, len(tags))
	for _, tag := range tags {
		tagNames = append(tagNames, tag.Name)
	}
	semver.Sort(tagNames)
	return tagNames[0], nil
}
