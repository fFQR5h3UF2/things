# Submission title: Minimum Window Substring
# Submission url  : https://leetcode.com/problems/minimum-window-substring/description/
# Submission url  : https://leetcode.com/submissions/detail/1165812156/
# Submission json : {"id":1165812156,"status_display":"Accepted","lang":"python3","question_id":76,"title_slug":"minimum-window-substring","code":"class Solution:\n    def minWindow(self, s: str, t: str) -> str:\n        if not s or not t:\n            return \"\"\n\n        dictT = defaultdict(int)\n        for c in t:\n            dictT[c] += 1\n\n        required = len(dictT)\n        l, r = 0, 0\n        formed = 0\n\n        windowCounts = defaultdict(int)\n        ans = [-1, 0, 0]\n\n        while r < len(s):\n            c = s[r]\n            windowCounts[c] += 1\n\n            if c in dictT and windowCounts[c] == dictT[c]:\n                formed += 1\n\n            while l <= r and formed == required:\n                c = s[l]\n\n                if ans[0] == -1 or r - l + 1 < ans[0]:\n                    ans[0] = r - l + 1\n                    ans[1] = l\n                    ans[2] = r\n\n                windowCounts[c] -= 1\n                if c in dictT and windowCounts[c] < dictT[c]:\n                    formed -= 1\n\n                l += 1\n\n            r += 1\n\n        return \"\" if ans[0] == -1 else s[ans[1]:ans[2] + 1]\n\n","title":"Minimum Window Substring","url":"/submissions/detail/1165812156/","lang_name":"Python3","time":"2 hours, 24 minutes","timestamp":1707049028,"status":10,"runtime":"91 ms","is_pending":"Not Pending","memory":"17.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dictT = defaultdict(int)
        for c in t:
            dictT[c] += 1

        required = len(dictT)
        l, r = 0, 0
        formed = 0

        windowCounts = defaultdict(int)
        ans = [-1, 0, 0]

        while r < len(s):
            c = s[r]
            windowCounts[c] += 1

            if c in dictT and windowCounts[c] == dictT[c]:
                formed += 1

            while l <= r and formed == required:
                c = s[l]

                if ans[0] == -1 or r - l + 1 < ans[0]:
                    ans[0] = r - l + 1
                    ans[1] = l
                    ans[2] = r

                windowCounts[c] -= 1
                if c in dictT and windowCounts[c] < dictT[c]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == -1 else s[ans[1] : ans[2] + 1]
