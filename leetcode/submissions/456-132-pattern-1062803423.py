# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062803423/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        for i in range(length):
            i_num = nums[i]
            for j in range(i + 1, length):
                j_num = nums[j]
                if j_num < i_num + 2:
                    continue
                for k in range(j + 1, length):
                    k_num = nums[k]
                    if i_num < k_num < j_num:
                        return True
        return False
