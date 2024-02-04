# Submission for Minimum Seconds to Equalize a Circular Array
# Submission url: https://leetcode.com/submissions/detail/1013067257/


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return 0

        max_nums = set(nums)

        if len(max_nums) == 1:
            return 0

        def calculate(max_num: int) -> int:
            left_to_convert = set(i for i in range(length) if nums[i] != max_num)
            seconds = 0
            while left_to_convert:
                to_remove = set()
                for i in range(length):
                    if i not in left_to_convert:
                        continue

                    if (i - 1 + length) % length not in left_to_convert or (
                        i + 1
                    ) % length not in left_to_convert:
                        to_remove.add(i)

                left_to_convert.difference_update(to_remove)
                seconds += 1

            return seconds

        return min(calculate(max_num) for max_num in max_nums)
