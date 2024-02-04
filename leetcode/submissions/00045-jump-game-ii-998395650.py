# Submission title: for Jump Game II
# Submission url  : https://leetcode.com/submissions/detail/998395650/
# Submission json : {"id": 998395650, "status_display": "Accepted", "lang": "python3", "question_id": 45, "title_slug": "jump-game-ii", "code": "class Solution:\n    def jump(self, nums: List[int]) -> int:\n        length = len(nums)\n        result = 0\n        end = 0\n        farthest = 0\n\n        for i in range(length - 1):\n            number = nums[i]\n            max_jump = i + number\n            if max_jump > farthest:\n                farthest = max_jump\n\n            if farthest >= length - 1:\n                result += 1\n                break\n            \n            if i == end:\n                result += 1\n                end = farthest\n\n\n        return result\n", "title": "Jump Game II", "url": "/submissions/detail/998395650/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689765590, "status": 10, "runtime": "128 ms", "is_pending": "Not Pending", "memory": "17.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0
        end = 0
        farthest = 0

        for i in range(length - 1):
            number = nums[i]
            max_jump = i + number
            if max_jump > farthest:
                farthest = max_jump

            if farthest >= length - 1:
                result += 1
                break

            if i == end:
                result += 1
                end = farthest

        return result
