LEETCODE_DIR = ${PACKAGE_DIR}/leetcode
LEETCODE_BASE_URL = https://leetcode.com
LEETCODE_SUBMISSIONS_FILE = ${LEETCODE_DIR}/submissions.json
LEETCODE_SUBMISSIONS_DIR = ${LEETCODE_DIR}/submissions/
LEETCODE_DATE = $(shell date '+%y-%m-%d')
LEETCODE_DOWNLOAD = ${OUT_TRACKER_DIR}/leetcode-download-${LEETCODE_DATE}
LEETCODE_BRANCH = dev/leetcode-update-${LEETCODE_DATE}
LEETCODE_COMMIT = feat(leetcode): add ${LEETCODE_DATE} submissions

.PHONY: leetcode
leetcode: leetcode/generate ## Run leetcode/parse

.PHONY: leetcode/download
leetcode/download: ${LEETCODE_DOWNLOAD} ## Download last 20 submissions to ./leetcode/submissions.json
${LEETCODE_DOWNLOAD}:
	"${LEETCODE_DIR}/scripts/download" "${LEETCODE_BASE_URL}" "${LEETCODE_SUBMISSIONS_FILE}" 20
	touch "${@}"

.PHONY: leetcode/generate
leetcode/generate: leetcode/download ## Generate files in ./leetcode/submissions/ from ./leetcode/submissions.json
	"${LEETCODE_DIR}/scripts/generate" "${LEETCODE_BASE_URL}" "${LEETCODE_SUBMISSIONS_FILE}" "${LEETCODE_SUBMISSIONS_DIR}"

.PHONY: leetcode/update
leetcode/update: ## Download new submissions, create MR for them, merge the MR
	git checkout -B "${LEETCODE_BRANCH}"
	$(MAKE) leetcode/generate leetcode/format
	git add "${LEETCODE_SUBMISSIONS_FILE}" "${LEETCODE_SUBMISSIONS_DIR}"
	git commit -m "${LEETCODE_COMMIT}"
	git push origin "${LEETCODE_BRANCH}"
	gh pr create --fill
	gh pr merge --admin --squash --delete-branch
	git checkout main
	git pull

.PHONY: leetcode/format
leetcode/format: leetcode/format-black leetcode/format-gofmt ## Run leetcode/format-black and leetcode/format-gofmt

.PHONY: leetcode/format-black
leetcode/format-black: leetcode/generate ## Format submissions using black
	poetry -C "${DOTFILES_DIR}" run black --quiet "${LEETCODE_SUBMISSIONS_DIR}"

.PHONY: leetcode/format-gofmt
leetcode/format-gofmt: leetcode/generate ## Format submissions using gofmt
	gofmt -w "${LEETCODE_SUBMISSIONS_DIR}"
