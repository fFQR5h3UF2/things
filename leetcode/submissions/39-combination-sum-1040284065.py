# Submission for Combination Sum
# Submission url: https://leetcode.com/submissions/detail/1040284065/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        cur_nums = []
        cur_sum = 0

        def backtrack() -> None:
            if cur_sum == target:
                result.append(cur_nums[:])
            if cur_sum > target:
                return

            for num in candidates:
                cur_nums.append(num)
                cur_sum += num

                backtrack()

                cur_sum -= num
                cur_num.pop()

        backtrack()

        return result
