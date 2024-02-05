leetcode_base_url = https://leetcode.com
leetcode_submissions_file = ./leetcode/submissions.json
leetcode_date = $(shell date '+%y-%m-%d')
leetcode_download = ${OUT_TRACKER_DIR}/leetcode-download-${leetcode_date}
leetcode_branch = dev/leetcode-update-${leetcode_date}
leetcode_commit = feat(leetcode): add ${leetcode_date} submissions

.PHONY: leetcode
leetcode: leetcode/generate ## Run leetcode/parse

.PHONY: leetcode/download
leetcode/download: ${leetcode_download} ## Download last 20 submissions to ./leetcode/submissions.json
${leetcode_download}:
	./leetcode/scripts/download "${leetcode_base_url}" "${leetcode_submissions_file}" 20
	touch "${@}"

.PHONY: leetcode/generate
leetcode/generate: leetcode/download ## Generate files in ./leetcode/submissions/ from ./leetcode/submissions.json
	./leetcode/scripts/generate "${leetcode_base_url}" "${leetcode_submissions_file}"

.PHONY: leetcode/update
leetcode/update: ## Download new submissions, create MR for them, merge the MR
	#git checkout -b "${leetcode_branch}"
	$(MAKE) leetcode/generate leetcode/format
	git add "${leetcode_submissions_file}" ./leetcode/submissions/
	git commit -m "${leetcode_commit}"
	git push
	gh pr create --title "${leetcode_commit}"
	gh pr --admin --squash --delete-branch
	git checkout main
	git pull

.PHONY: leetcode/format
leetcode/format: leetcode/format-black leetcode/format-gofmt ## Run leetcode/format-black and leetcode/format-gofmt

.PHONY: leetcode/format-black
leetcode/format-black: leetcode/generate ## Format submissions using black
	poetry run black --quiet ./leetcode/submissions/

.PHONY: leetcode/format-gofmt
leetcode/format-gofmt: leetcode/generate ## Format submissions using gofmt
	gofmt -w ./leetcode/submissions/
