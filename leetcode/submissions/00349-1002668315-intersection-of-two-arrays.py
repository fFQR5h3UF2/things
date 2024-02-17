# Submission title: Intersection of Two Arrays
# Submission url  : https://leetcode.com/problems/intersection-of-two-arrays/description/"
# Submission url  : https://leetcode.com/submissions/detail/1002668315/"


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(nums2)
