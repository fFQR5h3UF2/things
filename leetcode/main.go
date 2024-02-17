package main

import (
	"context"
	"fmt"
	"os"

	"shishifubing.com/leetcode/cmd"
)

func main() {
	ctx := context.Background()
	if err := cmd.Run(ctx, os.Args[1:], os.Getenv, os.Stdin, os.Stdout, os.Stderr); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
