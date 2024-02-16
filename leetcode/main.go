package main

import (
	"context"
	"log/slog"
	"os"

	"shishifubing.com/leetcode/cmd"
)

func main() {
	ctx := context.Background()
	if err := cmd.Run(ctx, os.Args[1:], os.Getenv, os.Stdin, os.Stdout, os.Stderr); err != nil {
		slog.Error(err.Error())
		os.Exit(1)
	}
}
