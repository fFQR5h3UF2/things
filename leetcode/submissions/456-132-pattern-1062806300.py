# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062806300/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        visited = set()
        unique_nums = []
        for num in nums:
            if num not in visited:
                unique_nums.append(num)
                visited.add(num)
        length = len(unique_nums)
        if length < 3:
            return False
        for i in range(length - 2):
            i_num = unique_nums[i]
            for j in range(i + 1, length - 1):
                j_num = unique_nums[j]
                if j_num < i_num + 2:
                    continue
                for k in range(j + 1, length):
                    k_num = unique_nums[k]
                    if i_num < k_num < j_num:
                        return True
        return False
