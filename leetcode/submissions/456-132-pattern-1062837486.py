# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062837486/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        if length < 3:
            return False
        nums_ids = {}
        nums_ids[nums[0]] = [0, 0]
        for k in range(1, length):
            k_num = nums[k]
            if k_num == nums[k - 1]:
                continue
            for i_num in nums_ids:
                if i_num >= k_num:
                    continue
                earliest_i = nums_ids[i_num][0]
                for j_num in nums_ids:
                    if j_num <= k_num:
                        continue
                    if earliest_i < nums_ids[j_num][1]:
                        return True
            if k_num in nums_ids:
                nums_ids[k_num][1] = k
            else:
                nums_ids[k_num] = [k, k]
        return False
