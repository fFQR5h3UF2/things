# Submission title: for Remove Element
# Submission url  : https://leetcode.com/submissions/detail/993596529/
# Submission json : {"id": 993596529, "status_display": "Accepted", "lang": "python3", "question_id": 27, "title_slug": "remove-element", "code": "class Solution:\n    # create two indexes, current and replace\n    # create non_val_count\n    # while to-be-replaced has not reached the end:\n    # - if the current number is a regular number, move the current index, \n    #   increase non_val_count\n    # - if the replace index is equal or less than the current, move it and continue\n    # - if the replace number is a non-regular number, move the replace index and continue\n    # - if the current number is a non-regular, replace it with the replace number, \n    #   replace the replace number with val, move both indexes\n    # return the current index + 1\n\n    def removeElement(self, nums: List[int], val: int) -> int:\n        current, replace, val_count, length = 0, 0, 0, len(nums)\n        non_val_count = 0\n        \n        while replace < length and current < length:\n            current_number, replace_number = nums[current], nums[replace]\n            \n            if current_number != val:\n                current += 1\n                non_val_count += 1\n                continue\n\n            if replace <= current:\n                replace = current + 1\n                continue\n\n            if replace_number == val:\n                replace += 1\n                continue\n\n            nums[current], nums[replace] = replace_number, val\n            replace += 1\n            current += 1\n            non_val_count += 1\n            \n        return non_val_count", "title": "Remove Element", "url": "/submissions/detail/993596529/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689263202, "status": 10, "runtime": "47 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # create two indexes, current and replace
    # create non_val_count
    # while to-be-replaced has not reached the end:
    # - if the current number is a regular number, move the current index,
    #   increase non_val_count
    # - if the replace index is equal or less than the current, move it and continue
    # - if the replace number is a non-regular number, move the replace index and continue
    # - if the current number is a non-regular, replace it with the replace number,
    #   replace the replace number with val, move both indexes
    # return the current index + 1

    def removeElement(self, nums: List[int], val: int) -> int:
        current, replace, val_count, length = 0, 0, 0, len(nums)
        non_val_count = 0

        while replace < length and current < length:
            current_number, replace_number = nums[current], nums[replace]

            if current_number != val:
                current += 1
                non_val_count += 1
                continue

            if replace <= current:
                replace = current + 1
                continue

            if replace_number == val:
                replace += 1
                continue

            nums[current], nums[replace] = replace_number, val
            replace += 1
            current += 1
            non_val_count += 1

        return non_val_count
