# Submission title: for Set Mismatch
# Submission url  : https://leetcode.com/submissions/detail/1055552901/
# Submission json : {"id": 1055552901, "status_display": "Accepted", "lang": "python3", "question_id": 645, "title_slug": "set-mismatch", "code": "class Solution:\n    def findErrorNums(self, nums: List[int]) -> List[int]:\n        n = len(nums)\n        dupl_xor_miss = 0\n        for i in range(1, n+1):\n            dupl_xor_miss ^= i ^ nums[i-1]\n        \n        # example for get rightmost set bit\n        # x:             01110000\n        # ~x:            10001111\n        # -x or ~x + 1:  10010000\n        # x & -x:        00010000\n\n        # example for unset rightmost set bit\n        # x:             01110000\n        # x-1:           01101111\n        # x & (x-1):     01100000\n        rightmost_set_bit = dupl_xor_miss & -dupl_xor_miss\n        xor_group1 = xor_group2 = 0\n        for i in range(1, n + 1):\n            if i & rightmost_set_bit:\n                xor_group1 ^= i\n            else:\n                xor_group2 ^= i\n            if nums[i-1] & rightmost_set_bit:\n                xor_group1 ^= nums[i-1]\n            else:\n                xor_group2 ^= nums[i-1]\n        \n        for num in nums:\n            if num == xor_group1:\n                return [num, xor_group2]\n            if num == xor_group2:\n                return [num, xor_group1]\n\n        return []", "title": "Set Mismatch", "url": "/submissions/detail/1055552901/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695312693, "status": 10, "runtime": "197 ms", "is_pending": "Not Pending", "memory": "17.6 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dupl_xor_miss = 0
        for i in range(1, n + 1):
            dupl_xor_miss ^= i ^ nums[i - 1]

        # example for get rightmost set bit
        # x:             01110000
        # ~x:            10001111
        # -x or ~x + 1:  10010000
        # x & -x:        00010000

        # example for unset rightmost set bit
        # x:             01110000
        # x-1:           01101111
        # x & (x-1):     01100000
        rightmost_set_bit = dupl_xor_miss & -dupl_xor_miss
        xor_group1 = xor_group2 = 0
        for i in range(1, n + 1):
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
                return [num, xor_group2]
            if num == xor_group2:
                return [num, xor_group1]

        return []
