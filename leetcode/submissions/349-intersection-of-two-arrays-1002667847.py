# Submission for Intersection of Two Arrays
# Submission url: https://leetcode.com/submissions/detail/1002667847/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & nums2
