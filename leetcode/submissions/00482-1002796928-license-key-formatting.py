# Submission title: License Key Formatting
# Submission url  : https://leetcode.com/problems/license-key-formatting/description/"
# Submission url  : https://leetcode.com/submissions/detail/1002796928/"


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        count = 0
        for letter in reversed(s):
            if letter == "-":
                continue

            if count == k:
                result.append("-")
                count = 0

            count += 1
            result.append(letter.upper())

        return "".join(reversed(result))
