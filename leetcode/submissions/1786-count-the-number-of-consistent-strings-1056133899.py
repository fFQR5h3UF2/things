# Submission for 'Count the Number of Consistent Strings'
# Submission url: https://leetcode.com/submissions/detail/1056133899/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            if not set(word) - allowed:
                count += 1
        return count
