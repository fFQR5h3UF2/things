# Submission for Minimum Seconds to Equalize a Circular Array
# Submission url: https://leetcode.com/submissions/detail/1013050540/


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return 0

        count = defaultdict(int)
        max_num = nums[0]
        for num in nums:
            count[num] += 1
            if count[num] > count[max_num]:
                max_num = num

        if len(count) == 1:
            return 0

        left_to_convert = set(i for i in range(length) if nums[i] != max_num)

        converted = set()
        seconds = 0

        while left_to_convert:
            for i in range(length):
                if i not in left_to_convert:
                    continue

                if (i - 1 + length) % length not in left_to_convert or (
                    i + 1
                ) % length not in left_to_convert:
                    left_to_convert.remove(i)

            seconds += 1

        return seconds
