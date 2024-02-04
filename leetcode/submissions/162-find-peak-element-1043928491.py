# Submission for Find Peak Element
# Submission url: https://leetcode.com/submissions/detail/1043928491/


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        num_count = len(nums)
        if num_count < 4:
            return sorted(enumerate(nums), key=lambda item: item[1])[-1][0]

        left, right = 0, num_count - 1

        while left < right:
            mid = left + (right - left) // 2
            num_left, num_mid, num_right = nums[mid - 1], nums[mid], nums[mid + 1]
            if num_left < num_mid > num_right:
                return mid

            if num_left > num_mid:
                right = mid
            else:
                left = mid

        return left
