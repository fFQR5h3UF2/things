# Submission title: for Maximum Length of Pair Chain
# Submission url  : https://leetcode.com/submissions/detail/1032115733/
# Submission json : {"id": 1032115733, "status_display": "Accepted", "lang": "python3", "question_id": 646, "title_slug": "maximum-length-of-pair-chain", "code": "class Solution:\n    def findLongestChain(self, pairs: List[List[int]]) -> int:\n        pairs_count = len(pairs)\n        if pairs_count < 2:\n            return pairs_count\n        \n        pairs.sort()\n        \n        @cache\n        def dp(curr_pair: int) -> int:\n            right = pairs[curr_pair][1]\n            max_length = 1\n\n            for new_pair in range(curr_pair + 1, pairs_count):\n                new_left = pairs[new_pair][0]\n                new_length = dp(new_pair) + (1 if new_left > right else 0)\n\n                if new_length > max_length:\n                    max_length = new_length\n            \n            return max_length\n        \n        return dp(0)", "title": "Maximum Length of Pair Chain", "url": "/submissions/detail/1032115733/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693041387, "status": 10, "runtime": "1564 ms", "is_pending": "Not Pending", "memory": "18.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs_count = len(pairs)
        if pairs_count < 2:
            return pairs_count

        pairs.sort()

        @cache
        def dp(curr_pair: int) -> int:
            right = pairs[curr_pair][1]
            max_length = 1

            for new_pair in range(curr_pair + 1, pairs_count):
                new_left = pairs[new_pair][0]
                new_length = dp(new_pair) + (1 if new_left > right else 0)

                if new_length > max_length:
                    max_length = new_length

            return max_length

        return dp(0)
