# Submission title: Find First and Last Position of Element in Sorted Array
# Submission url  : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1087553185/
# Submission json : {"id":1087553185,"status_display":"Accepted","lang":"python3","question_id":34,"title_slug":"find-first-and-last-position-of-element-in-sorted-array","code":"class Solution:\n    def searchRange(self, nums: List[int], target: int) -> List[int]:\n        def binary_search(nums, target, left):\n            low, high = 0, len(nums) - 1\n            index = -1\n            while low <= high:\n                mid = (low + high) // 2\n                if nums[mid] == target:\n                    index = mid\n                    if left:\n                        high = mid - 1\n                    else:\n                        low = mid + 1\n                elif nums[mid] < target:\n                    low = mid + 1\n                else:\n                    high = mid - 1\n            return index\n\n        left_index = binary_search(nums, target, left=True)\n        right_index = binary_search(nums, target, left=False)\n\n        return [left_index, right_index]","title":"Find First and Last Position of Element in Sorted Array","url":"/submissions/detail/1087553185/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698671798,"status":10,"runtime":"82 ms","is_pending":"Not Pending","memory":"17.7 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, left):
            low, high = 0, len(nums) - 1
            index = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    index = mid
                    if left:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return index

        left_index = binary_search(nums, target, left=True)
        right_index = binary_search(nums, target, left=False)

        return [left_index, right_index]
