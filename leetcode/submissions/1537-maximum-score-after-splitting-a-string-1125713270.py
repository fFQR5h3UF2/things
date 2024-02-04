# Submission for Maximum Score After Splitting a String
# Submission url: https://leetcode.com/submissions/detail/1125713270/


class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for char in s:
            if char == "1":
                score += 1
        max_score = score
        for char in s:
            if char == "0":
                score += 1
            else:
                score -= 1
            max_score = max(max_score, score)
        return max_score
