package model

import (
	"embed"
	"encoding/json"
	"fmt"
	"text/template"
)

//go:embed config.json submission.txt.tmpl
var embedFS embed.FS

func DefaultConfig() (*Config, error) {
	content, err := embedFS.ReadFile("config.json")
	if err != nil {
		return nil, fmt.Errorf("could not open embedded config: %w", err)
	}
	config := &Config{}
	err = json.Unmarshal(content, config)
	if err != nil {
		return nil, fmt.Errorf("could not parse embedded config: %w", err)
	}
	return config, nil
}

func SubmissionTemplate() (*template.Template, error) {
	templ, err := template.ParseFS(embedFS, "submission.txt.tmpl")
	if err != nil {
		return nil, fmt.Errorf("could not parse embedded template: %w", err)
	}
	return templ, nil
}
