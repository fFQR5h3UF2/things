package main

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"log/slog"
	"reflect"
	"testing"
	"time"

	"github.com/go-git/go-git/v5"
	"github.com/go-git/go-git/v5/plumbing/object"
)

func MockLogger() (*slog.Logger, *bytes.Buffer) {
	buff := &bytes.Buffer{}
	return slog.New(slog.NewTextHandler(buff, &slog.HandlerOptions{Level: slog.LevelDebug})), buff
}

func MockVersionService() *VersionService {
	logger, _ := MockLogger()
	return &VersionService{logger}
}

func TestRun(t *testing.T) {
	type args struct {
		ctx    context.Context
		args   []string
		getenv func(string) string
		stdin  io.Reader
	}
	tests := []struct {
		name       string
		args       args
		wantStdout string
		wantStderr string
		wantErr    bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			stdout := &bytes.Buffer{}
			stderr := &bytes.Buffer{}
			if err := Run(tt.args.ctx, tt.args.args, tt.args.getenv, tt.args.stdin, stdout, stderr); (err != nil) != tt.wantErr {
				t.Errorf("Run() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if gotStdout := stdout.String(); gotStdout != tt.wantStdout {
				t.Errorf("Run() = %v, want %v", gotStdout, tt.wantStdout)
			}
			if gotStderr := stderr.String(); gotStderr != tt.wantStderr {
				t.Errorf("Run() = %v, want %v", gotStderr, tt.wantStderr)
			}
		})
	}
}

func TestVersionService_FilterTags(t *testing.T) {
	type args struct {
		repo   *git.Repository
		filter func(tag *object.Tag) (bool, error)
	}
	tests := []struct {
		name    string
		s       *VersionService
		args    args
		want    []*object.Tag
		wantErr bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := tt.s.FilterTags(nil, tt.args.repo, tt.args.filter)
			if (err != nil) != tt.wantErr {
				t.Errorf("VersionService.FilterTags() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("VersionService.FilterTags() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestVersionService_FilterTagSemver(t *testing.T) {
	type args struct {
		tag *object.Tag
	}
	tests := []struct {
		name    string
		s       *VersionService
		args    args
		want    bool
		wantErr bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := tt.s.FilterTagSemver(tt.args.tag)
			if (err != nil) != tt.wantErr {
				t.Errorf("VersionService.FilterTagSemver() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if got != tt.want {
				t.Errorf("VersionService.FilterTagSemver() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestVersionService_CurrentVersion(t *testing.T) {
	type args struct {
		repo   *git.Repository
		filter TagFilter
	}
	tests := []struct {
		name    string
		s       *VersionService
		args    args
		want    string
		wantErr bool
	}{
		// TODO: Add test cases.
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := tt.s.CurrentVersion(nil, tt.args.repo, tt.args.filter)
			if (err != nil) != tt.wantErr {
				t.Errorf("VersionService.CurrentVersion() error = %v, wantErr %v", err, tt.wantErr)
				return
			}
			if got != tt.want {
				t.Errorf("VersionService.CurrentVersion() = %v, want %v", got, tt.want)
			}
		})
	}
}

func TestVersionService_NewVersion(t *testing.T) {
	now := time.Now()
	year, week := now.ISOWeek()
	want := fmt.Sprintf("%d.%d.0", year, week)
	tests := []struct {
		name string
		s    *VersionService
		want string
	}{
		{"Basic check", MockVersionService(), want},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := tt.s.NewVersion(); got != tt.want {
				t.Errorf("VersionService.NewVersion() = %v, want %v", got, tt.want)
			}
		})
	}
}
