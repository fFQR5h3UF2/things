# Submission title: Missing Number
# Submission url  : https://leetcode.com/problems/missing-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1054605267/
# Submission json : {"id":1054605267,"status_display":"Accepted","lang":"python3","question_id":268,"title_slug":"missing-number","code":"class Solution:\n    def missingNumber(self, nums: List[int]) -> int:\n        def xor(total: int, i: int) -> int:\n            return total ^ nums[i] ^ (i + 1)\n        return reduce(xor, chain((0, ), range(len(nums))))","title":"Missing Number","url":"/submissions/detail/1054605267/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695222159,"status":10,"runtime":"126 ms","is_pending":"Not Pending","memory":"17.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def xor(total: int, i: int) -> int:
            return total ^ nums[i] ^ (i + 1)

        return reduce(xor, chain((0,), range(len(nums))))
