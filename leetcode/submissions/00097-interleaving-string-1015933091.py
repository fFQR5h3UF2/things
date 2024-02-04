# Submission title: for Interleaving String
# Submission url  : https://leetcode.com/submissions/detail/1015933091/
# Submission json : {"id": 1015933091, "status_display": "Accepted", "lang": "python3", "question_id": 97, "title_slug": "interleaving-string", "code": "class Solution:\n    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:\n        length_1, length_2, length_3 = len(s1), len(s2), len(s3)\n        if length_1 + length_2 != length_3:\n            return False\n        \n        @cache\n        def dp(i_1: int, i_2: int, i_3: int) -> bool:\n            if i_3 == length_3:\n                return True\n\n            target = s3[i_3]\n            return (\n                i_1 != length_1 and s1[i_1] == target and dp(i_1 + 1, i_2, i_3 + 1)\n            ) or (\n                i_2 != length_2 and s2[i_2] == target and dp(i_1, i_2 + 1, i_3 + 1)\n            )\n\n        return dp(0, 0, 0)\n", "title": "Interleaving String", "url": "/submissions/detail/1015933091/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691519261, "status": 10, "runtime": "44 ms", "is_pending": "Not Pending", "memory": "17.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        length_1, length_2, length_3 = len(s1), len(s2), len(s3)
        if length_1 + length_2 != length_3:
            return False

        @cache
        def dp(i_1: int, i_2: int, i_3: int) -> bool:
            if i_3 == length_3:
                return True

            target = s3[i_3]
            return (
                i_1 != length_1 and s1[i_1] == target and dp(i_1 + 1, i_2, i_3 + 1)
            ) or (i_2 != length_2 and s2[i_2] == target and dp(i_1, i_2 + 1, i_3 + 1))

        return dp(0, 0, 0)
