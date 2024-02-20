# Submission title: Count the Number of Consistent Strings
# Submission url  : https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
# Submission url  : https://leetcode.com/submissions/detail/1056137764/"


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count
