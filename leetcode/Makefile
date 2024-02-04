leetcode_base_url = https://leetcode.com
leetcode_submissions_file = ./leetcode/submissions.json

.PHONY: leetcode/download
leetcode/download: ## Download last 20 submissions to submissions.json
	./leetcode/scripts/download "${leetcode_base_url}" "${leetcode_submissions_file}" \
		20

.PHONY: leetcode/download-custom
leetcode/download-custom: ## Download ${LEETCODE_COUNT} submissions from ${LEETCODE_OFFSET} to submissions.json
	./leetcode/scripts/download "${leetcode_base_url}" "${leetcode_submissions_file}" \
		"$${LEETCODE_COUNT}" "$${LEETCODE_OFFSET}"

.PHONY: leetcode/parse
leetcode/parse: ## Parse submissions.json and create files in submissions/
	./leetcode/scripts/parse "${leetcode_base_url}" "${leetcode_submissions_file}"

.PHONY: leetcode/format
leetcode/format: leetcode/format-black leetcode/format-gofmt ## Format submissions using black and gofmt

.PHONY: leetcode/format-black
leetcode/format-black: leetcode/parse ## Format submissions using black
	poetry run black leetcode/submissions

.PHONY: leetcode/format-gofmt
leetcode/format-gofmt: leetcode/parse ## Format submissions using gofmt
	gofmt -w leetcode/submissions
