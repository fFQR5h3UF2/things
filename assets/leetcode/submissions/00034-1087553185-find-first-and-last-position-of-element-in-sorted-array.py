# Submission title: Find First and Last Position of Element in Sorted Array
# Submission url  : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1087553185/"


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
