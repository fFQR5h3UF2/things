# Submission title: for Remove Element
# Submission url  : https://leetcode.com/submissions/detail/993600998/
# Submission json : {"id": 993600998, "status_display": "Accepted", "lang": "python3", "question_id": 27, "title_slug": "remove-element", "code": "class Solution:\n    # create replace index\n    # iterate over nums:\n    # - if the current number is equal to val, continue\n    # - set nums[replace] to that number, increase the index\n\n    def removeElement(self, nums: List[int], val: int) -> int:\n        replace = 0\n        for i, number in enumerate(nums):\n            if number == val:\n                continue\n            nums[replace] = number\n            replace += 1\n        \n        return replace", "title": "Remove Element", "url": "/submissions/detail/993600998/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689263564, "status": 10, "runtime": "44 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # create replace index
    # iterate over nums:
    # - if the current number is equal to val, continue
    # - set nums[replace] to that number, increase the index

    def removeElement(self, nums: List[int], val: int) -> int:
        replace = 0
        for i, number in enumerate(nums):
            if number == val:
                continue
            nums[replace] = number
            replace += 1

        return replace
