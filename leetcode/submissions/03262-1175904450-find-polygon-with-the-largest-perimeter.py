# Submission title: Find Polygon With the Largest Perimeter
# Submission url  : https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/description/
# Submission url  : https://leetcode.com/submissions/detail/1175904450/"


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        previous_elements_sum = 0
        ans = -1
        for num in nums:
            if num < previous_elements_sum:
                ans = num + previous_elements_sum
            previous_elements_sum += num
        return ans
