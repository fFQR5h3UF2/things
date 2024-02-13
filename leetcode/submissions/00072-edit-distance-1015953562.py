# Submission title: Edit Distance
# Submission url  : https://leetcode.com/problems/edit-distance/description/
# Submission url  : https://leetcode.com/submissions/detail/1015953562/
# Submission json : {"id":1015953562,"status_display":"Accepted","lang":"python3","question_id":72,"title_slug":"edit-distance","code":"class Solution:\n    def minDistance(self, word1: str, word2: str) -> int:\n        length1, length2 = len(word1), len(word2)\n\n        @cache\n        def dp(i1: int, i2: int) -> int:\n            if i1 == length1:\n                return length2 - (i2 + 1)\n\n            if i2 == length2:\n                return length1 - (i1 + 1)\n            \n            if word1[i1] == word2[i2]:\n                return dp(i1 + 1, i2 + 1)\n\n            return 1 + min((\n                # replace or insert\n                dp(i1 + 1, i2 + 1),\n                # remove from i1\n                dp(i1 + 1, i2),\n                # remove from i2\n                dp(i1, i2 + 1)\n            ))\n        \n        return dp(0, 0) + 1","title":"Edit Distance","url":"/submissions/detail/1015953562/","lang_name":"Python3","time":"5 months, 4 weeks","timestamp":1691520630,"status":10,"runtime":"82 ms","is_pending":"Not Pending","memory":"18.9 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1, length2 = len(word1), len(word2)

        @cache
        def dp(i1: int, i2: int) -> int:
            if i1 == length1:
                return length2 - (i2 + 1)

            if i2 == length2:
                return length1 - (i1 + 1)

            if word1[i1] == word2[i2]:
                return dp(i1 + 1, i2 + 1)

            return 1 + min(
                (
                    # replace or insert
                    dp(i1 + 1, i2 + 1),
                    # remove from i1
                    dp(i1 + 1, i2),
                    # remove from i2
                    dp(i1, i2 + 1),
                )
            )

        return dp(0, 0) + 1
