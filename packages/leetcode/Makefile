LEETCODE_DIR = ${PROJECT_DIR}/packages/leetcode
LEETCODE_BASE_URL = https://leetcode.com
LEETCODE_SUBMISSIONS_FILE = ${LEETCODE_DIR}/submissions.json
LEETCODE_SUBMISSIONS_DIR = ${LEETCODE_DIR}/submissions/
LEETCODE_DATE = $(shell date '+%y-%m-%d')
LEETCODE_DOWNLOAD = ${OUT_TRACKER_DIR}/leetcode-download-${LEETCODE_DATE}
LEETCODE_BRANCH = dev/leetcode-update-${LEETCODE_DATE}
LEETCODE_COMMIT = feat(leetcode): add ${LEETCDOE_DATE} submissions

.PHONY: packages/leetcode
packages/leetcode: packages/leetcode/generate ## Run leetcode/parse

.PHONY: packages/leetcode/download
packages/leetcode/download: ${LEETCODE_DOWNLOAD} ## Download last 20 submissions to ./leetcode/submissions.json
${LEETCODE_DOWNLOAD}:
	"${LEETCODE_DIR}/scripts/download" "${LEETCODE_BASE_URL}" "${LEETCODE_SUBMISSIONS_FILE}" 20
	touch "${@}"

.PHONY: packages/leetcode/generate
packages/leetcode/generate: packages/leetcode/download ## Generate files in ./leetcode/submissions/ from ./leetcode/submissions.json
	"${LEETCODE_DIR}/scripts/generate" "${LEETCODE_BASE_URL}" "${LEETCODE_SUBMISSIONS_FILE}" "${LEETCODE_SUBMISSIONS_DIR}"

.PHONY: packages/leetcode/update
packages/leetcode/update: ## Download new submissions, create MR for them, merge the MR
	git checkout -B "${LEETCODE_BRANCH}"
	$(MAKE) leetcode/generate leetcode/format
	git add "${LEETCODE_SUBMISSIONS_FILE}" "${LEETCODE_SUBMISSIONS_DIR}"
	git commit -m "${LEETCODE_COMMIT}"
	git push origin "${LEETCODE_BRANCH}"
	gh pr create --fill
	gh pr merge --admin --squash --delete-branch
	git checkout main
	git pull

.PHONY: packages/leetcode/format
packages/leetcode/format: packages/leetcode/format-black packages/leetcode/format-gofmt ## Run leetcode/format-black and leetcode/format-gofmt

.PHONY: packages/leetcode/format-black
packages/leetcode/format-black: packages/leetcode/generate ## Format submissions using black
	poetry run black --quiet "${LEETCODE_SUBMISSIONS_DIR}"

.PHONY: packages/leetcode/format-gofmt
packages/leetcode/format-gofmt: packages/leetcode/generate ## Format submissions using gofmt
	gofmt -w "${LEETCODE_SUBMISSIONS_DIR}"
