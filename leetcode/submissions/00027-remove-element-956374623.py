# Submission title: for Remove Element
# Submission url  : https://leetcode.com/submissions/detail/956374623/
# Submission json : {"id": 956374623, "status_display": "Accepted", "lang": "python3", "question_id": 27, "title_slug": "remove-element", "code": "class Solution:\n    def removeElement(self, nums: List[int], val: int) -> int:\n        length = len(nums)\n\n        if not length: \n            return 0\n\n        first = nums[0]\n        if length == 1 and first == val:\n            nums.pop()\n            return 0\n        if length == 1 and first != val:\n            return 1\n        \n        not_equal_index = -1 if first == val else 0\n        for i, number in enumerate(nums[1:], 1):\n            if number == val:\n                continue\n\n            not_equal_index += 1\n            nums[not_equal_index] = number\n\n        return not_equal_index + 1\n            \n\n", "title": "Remove Element", "url": "/submissions/detail/956374623/", "lang_name": "Python3", "time": "8\u00a0months, 2\u00a0weeks", "timestamp": 1684923903, "status": 10, "runtime": "47 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)

        if not length:
            return 0

        first = nums[0]
        if length == 1 and first == val:
            nums.pop()
            return 0
        if length == 1 and first != val:
            return 1

        not_equal_index = -1 if first == val else 0
        for i, number in enumerate(nums[1:], 1):
            if number == val:
                continue

            not_equal_index += 1
            nums[not_equal_index] = number

        return not_equal_index + 1
