# Submission title: for Remove Duplicates from Sorted Array
# Submission url  : https://leetcode.com/submissions/detail/956368066/
# Submission json : {"id": 956368066, "status_display": "Accepted", "lang": "python3", "question_id": 26, "title_slug": "remove-duplicates-from-sorted-array", "code": "class Solution:\n    def removeDuplicates(self, nums: List[int]) -> int:\n        length = len(nums)\n        if length == 1:\n            return 1\n        \n        unique_count = 1\n        last_unique_index = 0\n        for i, number in enumerate(nums[1:], 1):\n            last_unique = nums[last_unique_index]\n            if number == last_unique:\n                continue\n            \n            unique_count += 1\n            last_unique_index += 1\n            nums[last_unique_index] = number\n\n        nums = nums[:last_unique_index+1]\n\n        return unique_count", "title": "Remove Duplicates from Sorted Array", "url": "/submissions/detail/956368066/", "lang_name": "Python3", "time": "8\u00a0months, 2\u00a0weeks", "timestamp": 1684923099, "status": 10, "runtime": "94 ms", "is_pending": "Not Pending", "memory": "18.1 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 1

        unique_count = 1
        last_unique_index = 0
        for i, number in enumerate(nums[1:], 1):
            last_unique = nums[last_unique_index]
            if number == last_unique:
                continue

            unique_count += 1
            last_unique_index += 1
            nums[last_unique_index] = number

        nums = nums[: last_unique_index + 1]

        return unique_count
