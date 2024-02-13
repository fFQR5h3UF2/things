# Submission title: Determine if Two Strings Are Close
# Submission url  : https://leetcode.com/problems/determine-if-two-strings-are-close/description/
# Submission url  : https://leetcode.com/submissions/detail/1146049646/
# Submission json : {"id":1146049646,"status_display":"Accepted","lang":"python3","question_id":1777,"title_slug":"determine-if-two-strings-are-close","code":"\nclass Solution:\n    def closeStrings(self, word1: str, word2: str) -> bool:\n        freq1 = [0] * 26\n        freq2 = [0] * 26\n\n        for ch in word1:\n            freq1[ord(ch) - ord('a')] += 1\n\n        for ch in word2:\n            freq2[ord(ch) - ord('a')] += 1\n\n        for i in range(26):\n            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):\n                return False\n\n        freq1.sort()\n        freq2.sort()\n\n        for i in range(26):\n            if freq1[i] != freq2[i]:\n                return False\n\n        return True\n\n","title":"Determine if Two Strings Are Close","url":"/submissions/detail/1146049646/","lang_name":"Python3","time":"3 weeks","timestamp":1705242448,"status":10,"runtime":"202 ms","is_pending":"Not Pending","memory":"18.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord("a")] += 1

        for ch in word2:
            freq2[ord(ch) - ord("a")] += 1

        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True
