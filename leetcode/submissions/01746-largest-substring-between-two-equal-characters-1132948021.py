# Submission title: Largest Substring Between Two Equal Characters
# Submission url  : https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
# Submission url  : https://leetcode.com/submissions/detail/1132948021/
# Submission json : {"id":1132948021,"status_display":"Accepted","lang":"python3","question_id":1746,"title_slug":"largest-substring-between-two-equal-characters","code":"class Solution:\n    def maxLengthBetweenEqualCharacters(self, s: str) -> int:\n        ans = -1\n        \n        for left in range(len(s)):\n            for right in range(left + 1, len(s)):\n                if s[left] == s[right]:\n                    ans = max(ans, right - left - 1)\n        \n        return ans","title":"Largest Substring Between Two Equal Characters","url":"/submissions/detail/1132948021/","lang_name":"Python3","time":"1 month","timestamp":1704017974,"status":10,"runtime":"67 ms","is_pending":"Not Pending","memory":"17.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    ans = max(ans, right - left - 1)

        return ans
