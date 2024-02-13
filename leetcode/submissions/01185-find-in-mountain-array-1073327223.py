# Submission title: Find in Mountain Array
# Submission url  : https://leetcode.com/problems/find-in-mountain-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1073327223/
# Submission json : {"id":1073327223,"status_display":"Accepted","lang":"python3","question_id":1185,"title_slug":"find-in-mountain-array","code":"class Solution:\n    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:\n        # Save the length of the mountain array\n        length = mountain_arr.length()\n\n        # 1. Find the index of the peak element\n        low = 1\n        high = length - 2\n        while low != high:\n            test_index = (low + high) // 2\n            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):\n                low = test_index + 1\n            else:\n                high = test_index\n        peak_index = low\n\n        # 2. Search in the strictly increasing part of the array\n        low = 0\n        high = peak_index\n        while low != high:\n            test_index = (low + high) // 2\n            if mountain_arr.get(test_index) < target:\n                low = test_index + 1\n            else:\n                high = test_index    \n        # Check if the target is present in the strictly increasing part\n        if mountain_arr.get(low) == target:\n            return low\n        \n        # 3. Otherwise, search in the strictly decreasing part\n        low = peak_index + 1\n        high = length - 1\n        while low != high:\n            test_index = (low + high) // 2\n            if mountain_arr.get(test_index) > target:\n                low = test_index + 1\n            else:\n                high = test_index\n        # Check if the target is present in the strictly decreasing part\n        if mountain_arr.get(low) == target:\n            return low\n        \n        # Target is not present in the mountain array\n        return -1","title":"Find in Mountain Array","url":"/submissions/detail/1073327223/","lang_name":"Python3","time":"3 months, 3 weeks","timestamp":1697101785,"status":10,"runtime":"34 ms","is_pending":"Not Pending","memory":"17 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        # Save the length of the mountain array
        length = mountain_arr.length()

        # 1. Find the index of the peak element
        low = 1
        high = length - 2
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < mountain_arr.get(test_index + 1):
                low = test_index + 1
            else:
                high = test_index
        peak_index = low

        # 2. Search in the strictly increasing part of the array
        low = 0
        high = peak_index
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) < target:
                low = test_index + 1
            else:
                high = test_index
        # Check if the target is present in the strictly increasing part
        if mountain_arr.get(low) == target:
            return low

        # 3. Otherwise, search in the strictly decreasing part
        low = peak_index + 1
        high = length - 1
        while low != high:
            test_index = (low + high) // 2
            if mountain_arr.get(test_index) > target:
                low = test_index + 1
            else:
                high = test_index
        # Check if the target is present in the strictly decreasing part
        if mountain_arr.get(low) == target:
            return low

        # Target is not present in the mountain array
        return -1
