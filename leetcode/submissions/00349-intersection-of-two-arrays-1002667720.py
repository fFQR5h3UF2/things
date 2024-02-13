# Submission title: Intersection of Two Arrays
# Submission url  : https://leetcode.com/problems/intersection-of-two-arrays/description/
# Submission url  : https://leetcode.com/submissions/detail/1002667720/
# Submission json : {"id":1002667720,"status_display":"Accepted","lang":"python3","question_id":349,"title_slug":"intersection-of-two-arrays","code":"class Solution:\n    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:\n        return set(nums1) & set(nums2)","title":"Intersection of Two Arrays","url":"/submissions/detail/1002667720/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690206972,"status":10,"runtime":"58 ms","is_pending":"Not Pending","memory":"16.7 MB","compare_result":"1111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
