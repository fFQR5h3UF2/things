# Submission title: Max Dot Product of Two Subsequences
# Submission url  : https://leetcode.com/problems/max-dot-product-of-two-subsequences/description/
# Submission url  : https://leetcode.com/submissions/detail/1069975520/"


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return dp(0, 0)
