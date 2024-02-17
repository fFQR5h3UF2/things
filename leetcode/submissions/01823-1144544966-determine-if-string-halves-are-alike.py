# Submission title: Determine if String Halves Are Alike
# Submission url  : https://leetcode.com/problems/determine-if-string-halves-are-alike/description/"
# Submission url  : https://leetcode.com/submissions/detail/1144544966/"


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string):
            vowels = set("aeiouAEIOU")
            return sum(1 for char in string if char in vowels)

        length = len(s)
        mid_point = length // 2

        first_half = s[:mid_point]
        second_half = s[mid_point:]

        return count_vowels(first_half) == count_vowels(second_half)
