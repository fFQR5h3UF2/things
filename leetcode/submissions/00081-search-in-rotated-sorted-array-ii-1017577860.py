# Submission title: Search in Rotated Sorted Array II
# Submission url  : https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1017577860/
# Submission json : {"id":1017577860,"status_display":"Accepted","lang":"python3","question_id":81,"title_slug":"search-in-rotated-sorted-array-ii","code":"class Solution:\n    def search(self, nums: List[int], target: int) -> bool:\n        left, right = 0, len(nums) - 1\n        \n        while left <= right:\n            mid = (left + right) // 2\n            \n            if nums[mid] == target:\n                return True\n            \n            if nums[mid] == nums[left]:\n                left += 1\n                continue\n\n            if nums[left] <= nums[mid]:\n                if nums[left] <= target < nums[mid]:\n                    right = mid - 1\n                else:\n                    left = mid + 1\n            else:\n                if nums[mid] < target <= nums[right]:\n                    left = mid + 1\n                else:\n                    right = mid - 1\n        \n        return False","title":"Search in Rotated Sorted Array II","url":"/submissions/detail/1017577860/","lang_name":"Python3","time":"5 months, 4 weeks","timestamp":1691676278,"status":10,"runtime":"50 ms","is_pending":"Not Pending","memory":"16.9 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[left]:
                left += 1
                continue

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
