# Submission title: Find the Index of the First Occurrence in a String
# Submission url  : https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# Submission url  : https://leetcode.com/submissions/detail/990972145/
# Submission json : {"id":990972145,"status_display":"Accepted","lang":"python3","question_id":28,"title_slug":"find-the-index-of-the-first-occurrence-in-a-string","code":"class Solution:\n    # check edge cases:\n    # - if length of the needle is less than the length of the haystack: -1\n    # - if strings are equal: 0\n    # - if length of the needle is equal to the length of the haystack, but \n    #   strings are not equal: -1\n    # iterate over haystack and needle cheking if a substring starting with the current symbol\n    # is equal to the needle\n    def strStr(self, haystack: str, needle: str) -> int:\n        length_needle, length_haystack = len(needle), len(haystack)\n        last_needle_index = length_needle - 1\n\n        if length_needle > length_haystack:\n            return -1\n        \n        if haystack == needle:\n            return 0\n\n        if length_needle == length_haystack:\n            return -1\n        \n        if needle == haystack:\n            return 0\n\n        for i, _ in enumerate(haystack):\n            current_needle = haystack[i:i+length_needle]\n            if current_needle == needle:\n                return i\n        return -1\n","title":"Find the Index of the First Occurrence in a String","url":"/submissions/detail/990972145/","lang_name":"Python3","time":"6 months, 4 weeks","timestamp":1688993947,"status":10,"runtime":"51 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # check edge cases:
    # - if length of the needle is less than the length of the haystack: -1
    # - if strings are equal: 0
    # - if length of the needle is equal to the length of the haystack, but
    #   strings are not equal: -1
    # iterate over haystack and needle cheking if a substring starting with the current symbol
    # is equal to the needle
    def strStr(self, haystack: str, needle: str) -> int:
        length_needle, length_haystack = len(needle), len(haystack)
        last_needle_index = length_needle - 1

        if length_needle > length_haystack:
            return -1

        if haystack == needle:
            return 0

        if length_needle == length_haystack:
            return -1

        if needle == haystack:
            return 0

        for i, _ in enumerate(haystack):
            current_needle = haystack[i : i + length_needle]
            if current_needle == needle:
                return i
        return -1
