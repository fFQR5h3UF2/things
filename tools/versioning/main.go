package main

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

func main() {
	ctx := context.Background()
	if err := Run(ctx, os.Args[1:], os.Getenv, os.Stdin, os.Stdout, os.Stderr); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

func Run(
	ctx context.Context,
	args []string,
	getenv func(string) string,
	stdin io.Reader,
	stdout, stderr io.Writer,
) error {
	loggerOpts := &slog.HandlerOptions{Level: slog.LevelInfo}
	logger := slog.New(slog.NewTextHandler(stderr, loggerOpts))
	svc := &VersionService{logger: logger}
	dir, err := os.Getwd()
	if err != nil {
		return fmt.Errorf("could not get current directory: %w", err)
	}
	repo, err := git.PlainOpen(dir)
	if err != nil {
		return fmt.Errorf("could not open %s: %w", dir, err)
	}
	ver, err := svc.CurrentVersion(ctx, repo, svc.FilterTagSemver)
	if err != nil {
		return fmt.Errorf("could not get version from %s: %w", dir, err)
	}
	fmt.Println(ver)
	return nil
}

type VersionService struct {
	logger *slog.Logger
}

type TagFilter func(tag *object.Tag) (bool, error)

func (s *VersionService) FilterTags(ctx context.Context, repo *git.Repository, filter TagFilter) ([]*object.Tag, error) {
	tags, err := repo.Tags()
	if err != nil {
		return nil, fmt.Errorf("could not get tags: %w", err)
	}
	res := []*object.Tag{}
	err = tags.ForEach(func(ref *plumbing.Reference) error {
		select {
		case _, ok := <-ctx.Done():
			if ok {
				return fmt.Errorf("context cancelled")
			}
		}
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

// NewVersion constructs a new version using current year and weak number
func (s *VersionService) NewVersion() string {
	now := time.Now()
	year, week := now.ISOWeek()
	return fmt.Sprintf("%d.%d.0", year, week)
}

// FilterTagSemver returns true if the name of the tag is valid semver
func (s *VersionService) FilterTagSemver(tag *object.Tag) (bool, error) {
	return semver.IsValid(tag.Name), nil
}

// CurrentVersion filters tags using TagFiler, sorts found tags using semver.Sort,
// then returns the last one
func (s *VersionService) CurrentVersion(ctx context.Context, repo *git.Repository, filter TagFilter) (string, error) {
	tags, err := s.FilterTags(ctx, repo, filter)
	if err != nil {
		return "", fmt.Errorf("could not filter tags: %w", err)
	}
	length := len(tags)
	s.logger.Info(fmt.Sprintf("filtered %d tags", length))
	if length == 0 {
		return s.NewVersion(), nil
	}
	tagNames := make([]string, length)
	for i, tag := range tags {
		tagNames[i] = tag.Name
	}
	semver.Sort(tagNames)
	return tagNames[length-1], nil
}
