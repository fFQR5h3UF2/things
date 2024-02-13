# Submission title: Missing Number
# Submission url  : https://leetcode.com/problems/missing-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1054604639/
# Submission json : {"id":1054604639,"status_display":"Accepted","lang":"python3","question_id":268,"title_slug":"missing-number","code":"class Solution:\n    def missingNumber(self, nums: List[int]) -> int:\n        return reduce(lambda total, i: total ^ nums[i] ^ (i + 1), chain((0, ), range(len(nums))))","title":"Missing Number","url":"/submissions/detail/1054604639/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695222110,"status":10,"runtime":"130 ms","is_pending":"Not Pending","memory":"17.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(
            lambda total, i: total ^ nums[i] ^ (i + 1), chain((0,), range(len(nums)))
        )
