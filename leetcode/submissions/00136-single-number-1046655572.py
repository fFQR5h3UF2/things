# Submission title: Single Number
# Submission url  : https://leetcode.com/problems/single-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1046655572/
# Submission json : {"id":1046655572,"status_display":"Accepted","lang":"python3","question_id":136,"title_slug":"single-number","code":"class Solution:\n    def singleNumber(self, nums: List[int]) -> int:\n        return reduce(xor, nums)","title":"Single Number","url":"/submissions/detail/1046655572/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694448359,"status":10,"runtime":"131 ms","is_pending":"Not Pending","memory":"19.1 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
