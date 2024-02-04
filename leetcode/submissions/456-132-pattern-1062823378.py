# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062823378/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            i_num = nums[i]
            j_min = i_num + 2
            for j in range(i + 1, length):
                j_num = nums[j]
                if j_num < j_min:
                    continue
                for k in range(j + 1, length):
                    if i_num < nums[k] < j_num:
                        return True
        return False
