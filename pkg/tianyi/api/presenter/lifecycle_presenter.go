package presenter

import (
	"fmt"
	"net/http"

	pkgError "shishifubing.com/pkg/tianyi/pkg/error"
)

func CouldNotMigrateDatabase(err error) error {
	return pkgError.NewWithCode(
		fmt.Errorf("could not migrate database: %w", err),
		http.StatusInternalServerError,
	)
}
