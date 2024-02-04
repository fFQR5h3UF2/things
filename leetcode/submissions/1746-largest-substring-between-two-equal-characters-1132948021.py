# Submission for 'Largest Substring Between Two Equal Characters'
# Submission url: https://leetcode.com/submissions/detail/1132948021/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1

        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    ans = max(ans, right - left - 1)

        return ans
