# Submission title: Sort Characters By Frequency
# Submission url  : https://leetcode.com/problems/sort-characters-by-frequency/description/"
# Submission url  : https://leetcode.com/submissions/detail/1168584325/"


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = -ord(char)
            counter[char] -= 100
        return "".join(sorted(s, key=lambda val: counter[val]))
