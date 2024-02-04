# Submission title: for Sort Array By Parity
# Submission url  : https://leetcode.com/submissions/detail/1061185383/
# Submission json : {"id": 1061185383, "status_display": "Accepted", "lang": "python3", "question_id": 941, "title_slug": "sort-array-by-parity", "code": "class Solution:\n    def sortArrayByParity(self, nums: List[int]) -> List[int]:\n        length = len(nums)\n        left, right = 0, length - 1\n        answer = [None] * length\n        for num in nums:\n            if num % 2 == 0:\n                answer[left] = num\n                left += 1\n            else:\n                answer[right] = num\n                right -= 1\n        return answer", "title": "Sort Array By Parity", "url": "/submissions/detail/1061185383/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695885196, "status": 10, "runtime": "79 ms", "is_pending": "Not Pending", "memory": "17 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left, right = 0, length - 1
        answer = [None] * length
        for num in nums:
            if num % 2 == 0:
                answer[left] = num
                left += 1
            else:
                answer[right] = num
                right -= 1
        return answer
