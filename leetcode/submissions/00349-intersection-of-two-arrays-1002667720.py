# Submission for Intersection of Two Arrays
# Submission url: https://leetcode.com/submissions/detail/1002667720/


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
