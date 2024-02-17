# Submission title: Sort Characters By Frequency
# Submission url  : https://leetcode.com/problems/sort-characters-by-frequency/description/"
# Submission url  : https://leetcode.com/submissions/detail/1168581047/"


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        return "".join(
            sorted(s, key=lambda val: -(ord(val) + counter[val] * 100))
        )
