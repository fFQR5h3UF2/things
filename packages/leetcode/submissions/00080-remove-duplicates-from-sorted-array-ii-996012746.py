# Submission title: for Remove Duplicates from Sorted Array II
# Submission url  : https://leetcode.com/submissions/detail/996012746/
# Submission json : {"id": 996012746, "status_display": "Accepted", "lang": "python3", "question_id": 80, "title_slug": "remove-duplicates-from-sorted-array-ii", "code": "class Solution:\n    def removeDuplicates(self, nums: List[int]) -> int:\n        length = len(nums)\n\n        if length < 2:\n            return length\n        \n        current_index = 2\n\n        for number in nums[2:]:\n            if number == nums[current_index-2]:\n                continue\n            \n            nums[current_index] = number\n            current_index += 1\n\n        return current_index", "title": "Remove Duplicates from Sorted Array II", "url": "/submissions/detail/996012746/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689524790, "status": 10, "runtime": "66 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)

        if length < 2:
            return length

        current_index = 2

        for number in nums[2:]:
            if number == nums[current_index - 2]:
                continue

            nums[current_index] = number
            current_index += 1

        return current_index
