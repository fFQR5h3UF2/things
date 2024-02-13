# Submission title: Make String a Subsequence Using Cyclic Increments
# Submission url  : https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/
# Submission url  : https://leetcode.com/submissions/detail/1025840714/
# Submission json : {"id":1025840714,"status_display":"Accepted","lang":"python3","question_id":3018,"title_slug":"make-string-a-subsequence-using-cyclic-increments","code":"class Solution:\n    def canMakeSubsequence(self, str1: str, str2: str) -> bool:\n        length1, length2 = len(str1), len(str2)\n        \n        for i in range(length1):\n            if i + length2 > length1:\n                break\n            \n            idx2 = 0\n            for idx1 in range(i, length1):\n                if ord(str2[idx2]) - ord(str1[idx1]) in (0, 1, -25):\n                    idx2 += 1\n                \n                if idx2 == length2:\n                    return True\n            \n            \n        return False","title":"Make String a Subsequence Using Cyclic Increments","url":"/submissions/detail/1025840714/","lang_name":"Python3","time":"5 months, 2 weeks","timestamp":1692457999,"status":10,"runtime":"110 ms","is_pending":"Not Pending","memory":"17.2 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        length1, length2 = len(str1), len(str2)

        for i in range(length1):
            if i + length2 > length1:
                break

            idx2 = 0
            for idx1 in range(i, length1):
                if ord(str2[idx2]) - ord(str1[idx1]) in (0, 1, -25):
                    idx2 += 1

                if idx2 == length2:
                    return True

        return False
