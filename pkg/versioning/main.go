package versioning

import (
	"context"
	"fmt"
	"io"
	"log/slog"
	"os"
	"time"

	"github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing"
	"github.com/go-git/go-git/v5/plumbing/object"
	"golang.org/x/mod/semver"
)

func Run(
	ctx context.Context,
	args []string,
	getenv func(string) string,
	stdin io.Reader,
	stdout, stderr io.Writer,
) error {
	logger := slog.New(slog.NewTextHandler(stderr, &slog.HandlerOptions{Level: slog.LevelInfo}))
	svc := &VersionService{logger: logger}
	dir, err := os.Getwd()
	if err != nil {
		return fmt.Errorf("could not get current directory: %w", err)
	}
	repo, err := git.PlainOpen(dir)
	if err != nil {
		return fmt.Errorf("could not open %s: %w", dir, err)
	}
	ver, err := svc.CurrentVersion(repo)
	if err != nil {
		return fmt.Errorf("could not get version from %s: %w", dir, err)
	}
	fmt.Println(ver)
	return nil
}

type VersionService struct {
	logger *slog.Logger
}

func (s *VersionService) FilterTags(repo *git.Repository, filter func(tag *object.Tag) (bool, error)) ([]*object.Tag, error) {
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

func (s *VersionService) NewVersion() (string, error) {
	now := time.Now()
	year, week := now.ISOWeek()
	return fmt.Sprintf("%s.%s.0", year, week), nil
}

func (s *VersionService) FilterTagSemver(tag *object.Tag) (bool, error) {
	return semver.IsValid(tag.Name), nil
}

func (s *VersionService) CurrentVersion(repo *git.Repository) (string, error) {
	tags, err := s.FilterTags(repo, s.FilterTagSemver)
	if err != nil {
		return "", fmt.Errorf("could not filter tags: %w", err)
	}
	length := len(tags)
	s.logger.Info(fmt.Sprintf("filtered %d tags", length))
	if length == 0 {
		return s.NewVersion()
	}
	tagNames := make([]string, length)
	for i, tag := range tags {
		tagNames[i] = tag.Name
	}
	semver.Sort(tagNames)
	return tagNames[length-1], nil
}
