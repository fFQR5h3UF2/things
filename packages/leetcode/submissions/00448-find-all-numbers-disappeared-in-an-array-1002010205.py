# Submission title: for Find All Numbers Disappeared in an Array
# Submission url  : https://leetcode.com/submissions/detail/1002010205/
# Submission json : {"id": 1002010205, "status_display": "Accepted", "lang": "python3", "question_id": 448, "title_slug": "find-all-numbers-disappeared-in-an-array", "code": "class Solution:\n    # [1,1,3,4], [1,2,3,4] -> [2]\n    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:\n        nums.sort()\n        result = []\n        length = len(nums)\n        j = 0\n        for i in range(1, length + 1):\n            while j < length and nums[j] < i:\n                j += 1\n            \n            if j < length and nums[j] == i:\n                continue\n\n            result.append(i)\n\n        return result\n", "title": "Find All Numbers Disappeared in an Array", "url": "/submissions/detail/1002010205/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690134957, "status": 10, "runtime": "399 ms", "is_pending": "Not Pending", "memory": "25.2 MB", "compare_result": "1111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # [1,1,3,4], [1,2,3,4] -> [2]
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []
        length = len(nums)
        j = 0
        for i in range(1, length + 1):
            while j < length and nums[j] < i:
                j += 1

            if j < length and nums[j] == i:
                continue

            result.append(i)

        return result
