leetcode_base_url = https://leetcode.com
leetcode_submissions_file = ./leetcode/submissions.json
leetcode_download = ${OUT_TRACKER_DIR}/leetcode-download-$(shell date '+%y.%m.%d')

.PHONY: leetcode
leetcode: leetcode/parse ## Run leetcode/parse

.PHONY: leetcode/download
leetcode/download: ${leetcode_download} ## Download last 20 submissions to ./leetcode/submissions.json
${leetcode_download}:
	./leetcode/scripts/download "${leetcode_base_url}" "${leetcode_submissions_file}" 20
	touch "${@}"

.PHONY: leetcode/parse
leetcode/parse: leetcode/download ## Generate files in ./leetcode/submissions/ from ./leetcode/submissions.json
	./leetcode/scripts/parse "${leetcode_base_url}" "${leetcode_submissions_file}"

.PHONY: leetcode/format
leetcode/format: leetcode/format-black leetcode/format-gofmt ## Run leetcode/format-black and leetcode/format-gofmt

.PHONY: leetcode/format-black
leetcode/format-black: leetcode/parse ## Format submissions using black
	poetry run black --quiet ./leetcode/submissions/

.PHONY: leetcode/format-gofmt
leetcode/format-gofmt: leetcode/parse ## Format submissions using gofmt
	gofmt -w ./leetcode/submissions/
