# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062818780/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        new_nums = [nums[0]]
        for num in nums[1:]:
            if num == new_nums[-1]:
                continue
            new_nums.append(num)
        length = len(new_nums)
        for k in range(3, length):
            k_num = new_nums[k]
            for j in reversed(range(1, k)):
                j_num = new_nums[j]
                if j_num <= k_num:
                    continue
                for i in range(j):
                    if new_nums[i] < k_num:
                        return True
        return False
