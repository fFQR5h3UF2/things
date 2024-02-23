package main

import (
	"context"
	"fmt"
	"os"

	"shishifubing.com/pkg/versioning"
)

func main() {
	ctx := context.Background()
	if err := versioning.Run(ctx, os.Args[1:], os.Getenv, os.Stdin, os.Stdout, os.Stderr); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
