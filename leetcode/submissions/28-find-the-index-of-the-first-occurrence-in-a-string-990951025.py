# Submission for Find the Index of the First Occurrence in a String
# Submission url: https://leetcode.com/submissions/detail/990951025/


class Solution:
    # check edge cases:
    # - if length of the needle is less than the length of the haystack: -1
    # - if strings are equal: 0
    # - if length of the needle is equal to the length of the haystack, but
    #   strings are not equal: -1
    # iterate over haystack and needle cheking if a symbol from haystack
    #   corresponds to the symbol in needle
    def strStr(self, haystack: str, needle: str) -> int:
        length_needle, length_haystack = len(needle), len(haystack)

        if length_needle > length_haystack:
            return -1

        if haystack == needle:
            return 0

        if length_needle == length_haystack:
            return -1

        j = 0
        for i, symbol_haystack in enumerate(haystack):
            if not needle[j] == symbol_haystack:
                j = 0
                continue

            if j == length_needle - 1:
                return i - j

            j += 1

        return -1
