# Submission title: Minimize the Maximum Difference of Pairs
# Submission url  : https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/
# Submission url  : https://leetcode.com/submissions/detail/1016434342/"


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        nums_count = len(nums)

        # Find the number of valid pairs by greedy approach
        def countValidPairs(threshold: int) -> int:
            index, count = 0, 0
            while index < nums_count - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count

        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1

        return left
