# Submission title: Single Number
# Submission url  : https://leetcode.com/problems/single-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1046649051/
# Submission json : {"id":1046649051,"status_display":"Accepted","lang":"python3","question_id":136,"title_slug":"single-number","code":"class Solution:\n    def singleNumber(self, nums: List[int]) -> int:\n        return reduce(lambda total, element: total ^ element, nums)","title":"Single Number","url":"/submissions/detail/1046649051/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694447895,"status":10,"runtime":"128 ms","is_pending":"Not Pending","memory":"19 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, element: total ^ element, nums)
