# Submission for Longest Arithmetic Subsequence of Given Difference
# Submission url: https://leetcode.com/submissions/detail/1012231579/



class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        length = len(arr)
        count = 0

        @cache
        def calculate(i: int) -> int
            if i == length:
                return 0

            max_count = 0
            for j in range(i + 1, length):
                if arr[j] - arr[i] != difference:
                    continue

                count = 1 + calculate(j)
                if count > max_count:
                    max_count = count

        return calculate(0)
