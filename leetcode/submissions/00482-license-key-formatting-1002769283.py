# Submission title: License Key Formatting
# Submission url  : https://leetcode.com/problems/license-key-formatting/description/
# Submission url  : https://leetcode.com/submissions/detail/1002769283/
# Submission json : {"id":1002769283,"status_display":"Accepted","lang":"python3","question_id":482,"title_slug":"license-key-formatting","code":"class Solution:\n    # \"5F3Z-2e-9-w\" -> \"5F3Z2E9W\" -> \"5F3Z2E9W\"\n    def licenseKeyFormatting(self, s: str, k: int) -> str:\n        letters = s.replace(\"-\", \"\").upper()\n        result = []\n        end = len(letters)\n        while end > 0:\n            start = end - k\n            if start < 0:\n                start = 0\n            result.append(letters[start:end])\n            end -= k\n\n        return \"-\".join(reversed(result))","title":"License Key Formatting","url":"/submissions/detail/1002769283/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690214534,"status":10,"runtime":"61 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"11111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # "5F3Z-2e-9-w" -> "5F3Z2E9W" -> "5F3Z2E9W"
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        letters = s.replace("-", "").upper()
        result = []
        end = len(letters)
        while end > 0:
            start = end - k
            if start < 0:
                start = 0
            result.append(letters[start:end])
            end -= k

        return "-".join(reversed(result))
