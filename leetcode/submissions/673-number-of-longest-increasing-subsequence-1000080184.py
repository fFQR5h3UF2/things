# Submission for Number of Longest Increasing Subsequence
# Submission url: https://leetcode.com/submissions/detail/1000080184/


class Solution:
    # [1,3,5,4,7] -> 2
    # [2,2,2,2,2] -> 5
    def findNumberOfLIS(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return length

        lengths = [1] * length
        counts = [1] * length

        for i in range(1, length):
            for j in range(i):
                if nums[i] < nums[j]:
                    continue

                length_start, length_end = lengths[j], lengths[i]
                count_start, count_end = counts[j], counts[i]

                if length_start + 1 > length_end:
                    lengths[i] = length_start + 1
                    counts[i] = count_start
                elif length_start + 1 == length_end:
                    counts[i] += count_start

        max_length = max(lengths)
        return sum(
            count for length, count in zip(lengths, counts) if length == max_length
        )
