# Submission title: Peak Index in a Mountain Array
# Submission url  : https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1003589521/"


class Solution:
    # [0,3,2,1,0]
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)

        left, right = 0, length - 1
        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left
