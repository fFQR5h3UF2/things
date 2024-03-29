package presenter

import (
	"fmt"
	"net/http"

	pkgError "shishifubing.com/pkg/tianyi/pkg/error"
)

func InvalidBranchName(err error) error {
	return pkgError.NewWithCode(
		fmt.Errorf("invalid branch name: %w", err), http.StatusBadRequest,
	)
}

func CouldNotFindProjectBranch(err error) error {
	return pkgError.NewWithCode(
		fmt.Errorf("could not find project branch(es): %w", err),
		http.StatusNotFound,
	)
}

func CouldNotCreateProjectBranch(err error) error {
	return pkgError.NewWithCode(
		fmt.Errorf("could not find create branch: %w", err),
		http.StatusNotFound,
	)
}
