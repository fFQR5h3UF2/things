# Submission title: Set Mismatch
# Submission url  : https://leetcode.com/problems/set-mismatch/description/
# Submission url  : https://leetcode.com/submissions/detail/1153445153/
# Submission json : {"id":1153445153,"status_display":"Accepted","lang":"python3","question_id":645,"title_slug":"set-mismatch","code":"class Solution:\n    def findErrorNums(self, nums: List[int]) -> List[int]:\n        length = len(nums)\n        # dupl_xor_miss = duplicate ^ missing\n        dupl_xor_miss = reduce(lambda total, i: total ^ i ^ nums[i - 1], range(length + 1))\n        rightmost_set_bit = dupl_xor_miss & -dupl_xor_miss\n        xor_group1 = xor_group2 = 0\n        for i in range(1, length + 1):\n            if i & rightmost_set_bit:\n                xor_group1 ^= i\n            else:\n                xor_group2 ^= i\n            if nums[i - 1] & rightmost_set_bit:\n                xor_group1 ^= nums[i - 1]\n            else:\n                xor_group2 ^= nums[i - 1]\n        for num in nums:\n            if num == xor_group1:\n                return num, xor_group2\n            if num == xor_group2:\n                return num, xor_group1 \n        \n        raise Exception()","title":"Set Mismatch","url":"/submissions/detail/1153445153/","lang_name":"Python3","time":"1 week, 6 days","timestamp":1705916345,"status":10,"runtime":"179 ms","is_pending":"Not Pending","memory":"17.9 MB","compare_result":"1111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        length = len(nums)
        # dupl_xor_miss = duplicate ^ missing
        dupl_xor_miss = reduce(
            lambda total, i: total ^ i ^ nums[i - 1], range(length + 1)
        )
        rightmost_set_bit = dupl_xor_miss & -dupl_xor_miss
        xor_group1 = xor_group2 = 0
        for i in range(1, length + 1):
            if i & rightmost_set_bit:
                xor_group1 ^= i
            else:
                xor_group2 ^= i
            if nums[i - 1] & rightmost_set_bit:
                xor_group1 ^= nums[i - 1]
            else:
                xor_group2 ^= nums[i - 1]
        for num in nums:
            if num == xor_group1:
                return num, xor_group2
            if num == xor_group2:
                return num, xor_group1

        raise Exception()
