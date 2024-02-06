# Submission title: for Permutations
# Submission url  : https://leetcode.com/submissions/detail/1057808743/
# Submission json : {"id": 1057808743, "status_display": "Accepted", "lang": "python3", "question_id": 46, "title_slug": "permutations", "code": "class Solution:\n    def permute(self, nums: List[int]) -> List[List[int]]:\n\n        length = len(nums)\n        current = []\n        current_contains = [False] * length\n\n        def backtrack() -> Generator[None, None, List[int]]:\n            if len(current) == length:\n                yield tuple(current[:])\n                return\n\n            for i in range(length):\n                if current_contains[i]:\n                    continue\n\n                current_contains[i] = True\n                current.append(nums[i])\n\n                yield from backtrack()\n\n                current_contains[i] = False\n                current.pop()\n            \n            return\n\n        return tuple(combination for combination in backtrack()) ", "title": "Permutations", "url": "/submissions/detail/1057808743/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695549340, "status": 10, "runtime": "48 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)
        current = []
        current_contains = [False] * length

        def backtrack() -> Generator[None, None, List[int]]:
            if len(current) == length:
                yield tuple(current[:])
                return

            for i in range(length):
                if current_contains[i]:
                    continue

                current_contains[i] = True
                current.append(nums[i])

                yield from backtrack()

                current_contains[i] = False
                current.pop()

            return

        return tuple(combination for combination in backtrack())
