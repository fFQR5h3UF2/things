# Submission title: Minimum Changes To Make Alternating Binary String
# Submission url  : https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/
# Submission url  : https://leetcode.com/submissions/detail/1127327445/
# Submission json : {"id":1127327445,"status_display":"Accepted","lang":"python3","question_id":1884,"title_slug":"minimum-changes-to-make-alternating-binary-string","code":"class Solution:\n    def minOperations(self, s: str) -> int:\n        start0 = 0\n        start1 = 0\n        \n        for i in range(len(s)):\n            if i % 2 == 0:\n                if s[i] == \"0\":\n                    start1 += 1\n                else:\n                    start0 += 1\n            else:\n                if s[i] == \"1\":\n                    start1 += 1\n                else:\n                    start0 += 1\n        \n        return min(start0, start1)","title":"Minimum Changes To Make Alternating Binary String","url":"/submissions/detail/1127327445/","lang_name":"Python3","time":"1 month, 1 week","timestamp":1703411654,"status":10,"runtime":"42 ms","is_pending":"Not Pending","memory":"17.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0
        start1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
                else:
                    start0 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                else:
                    start0 += 1

        return min(start0, start1)
