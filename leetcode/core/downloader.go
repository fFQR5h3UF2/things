package core

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"net/url"
	"strings"

	"shishifubing.com/leetcode/model"
)

const SUBMISSIONS_REQUEST_LIMIT = 20

type Downloader struct {
	config *model.Config
	client *http.Client
	ctx    context.Context
	logger *slog.Logger
}

func NewDownloader(config *model.Config, ctx context.Context, logger *slog.Logger) (*Downloader, error) {
	if config.Session == "" {
		return nil, fmt.Errorf("missing cookie in the config")
	}
	downloader := &Downloader{
		config: config,
		client: &http.Client{},
		ctx:    ctx,
		logger: logger,
	}
	return downloader, nil
}

func (d *Downloader) GetSubmissions(offset uint64, limit uint64) ([]*model.Submission, error) {
	res := []*model.Submission{}
	for limit > 0 {
		count := min(limit, SUBMISSIONS_REQUEST_LIMIT)
		response, err := d.getSubmissions(offset, count)
		if err != nil {
			return nil, fmt.Errorf("could not get submissions %d-%d: %w", offset, limit, err)
		}
		res = append(res, response.SubmissionsDump...)
		offset += count
		limit -= count
	}
	d.logger.Info(fmt.Sprintf("fetched %d submissions with offset %d", offset, limit))
	return res, nil
}

func (d *Downloader) getSubmissions(offset uint64, limit uint64) (*model.SubmissonsResponse, error) {
	reqUrl, err := url.Parse(strings.Join([]string{d.config.BaseUrl, "api", "submissions"}, "/"))
	if err != nil {
		return nil, fmt.Errorf("request '%s' failed: %w", reqUrl, err)
	}
	query := reqUrl.Query()
	query.Set("offset", fmt.Sprint(offset))
	query.Set("limit", fmt.Sprint(limit))
	query.Set("lastkey", "")
	reqUrl.RawQuery = query.Encode()
	request, err := http.NewRequest("GET", reqUrl.String(), nil)
	if err != nil {
		return nil, fmt.Errorf("request '%s' failed: %w", reqUrl, err)
	}
	request.Header.Set("content-type", "application/json; charset=utf-8")
	request.Header.Set("origin", d.config.BaseUrl)
	request.Header.Set("referer", d.config.BaseUrl)
	request.Header.Set("user-agent", "Mozilla/5.0 LeetCode API")
	request.Header.Set("cookie", fmt.Sprintf("LEETCODE_SESSION=%s", d.config.Session))

	response, err := d.client.Do(request)
	if err != nil {
		return nil, fmt.Errorf("request '%s' failed: %w", reqUrl, err)
	}
	defer response.Body.Close()
	body, err := io.ReadAll(response.Body)
	if err != nil {
		return nil, fmt.Errorf("request '%s' failed with '%s': %w", reqUrl, response.StatusCode, err)
	}
	bodyJson := &model.SubmissonsResponse{}
	err = json.Unmarshal(body, bodyJson)
	if err != nil {
		return nil, fmt.Errorf("request '%s' failed with '%s' and response '%s': %w", reqUrl, response.StatusCode, body, err)
	}
	if response.StatusCode != 200 {
		return nil, fmt.Errorf("request '%s' failed with '%s' and response '%s'", reqUrl, response.StatusCode, body)
	}
	return bodyJson, nil
}
