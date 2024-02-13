# Submission title: Decoded String at Index
# Submission url  : https://leetcode.com/problems/decoded-string-at-index/description/
# Submission url  : https://leetcode.com/submissions/detail/1060597351/
# Submission json : {"id":1060597351,"status_display":"Accepted","lang":"python3","question_id":916,"title_slug":"decoded-string-at-index","code":"class Solution:\n    def decodeAtIndex(self, s: str, k: int) -> str:\n        length = 0\n        i = 0\n        \n        while length < k:\n            if s[i].isdigit():\n                length *= int(s[i])\n            else:\n                length += 1\n            i += 1\n        \n        for j in range(i-1, -1, -1):\n            char = s[j]\n            if char.isdigit():\n                length //= int(char)\n                k %= length\n            else:\n                if k == 0 or k == length:\n                    return char\n                length -= 1","title":"Decoded String at Index","url":"/submissions/detail/1060597351/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695827480,"status":10,"runtime":"36 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0
        i = 0

        while length < k:
            if s[i].isdigit():
                length *= int(s[i])
            else:
                length += 1
            i += 1

        for j in range(i - 1, -1, -1):
            char = s[j]
            if char.isdigit():
                length //= int(char)
                k %= length
            else:
                if k == 0 or k == length:
                    return char
                length -= 1
