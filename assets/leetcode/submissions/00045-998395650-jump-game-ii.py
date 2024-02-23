# Submission title: Jump Game II
# Submission url  : https://leetcode.com/problems/jump-game-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/998395650/"


class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0
        end = 0
        farthest = 0

        for i in range(length - 1):
            number = nums[i]
            max_jump = i + number
            if max_jump > farthest:
                farthest = max_jump

            if farthest >= length - 1:
                result += 1
                break

            if i == end:
                result += 1
                end = farthest

        return result
