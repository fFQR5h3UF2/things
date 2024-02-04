# Submission for Interleaving String
# Submission url: https://leetcode.com/submissions/detail/1031178949/



class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        length_1, length_2, length_3 = len(s1), len(s2), len(s3)
        if length_1 + length_2 != length_3:
            return False

        dp = [[[False] * length_3 for _ in range(length_3)] for _ in range(length_3)]
        dp[0][0][0] = s1[0] == s3[0]
        dp[0][1][0]
        i_3 = 0

        for i_1 in range(0, length_1):

            for i_2 in range(0, length_2):
                for i_3 in range(0, length_3):


        return dp[-1][-1][-1]

        @cache
        def dp(i_1: int, i_2: int, i_3: int) -> bool:
            if i_3 == length_3:
                return True

            target = s3[i_3]
            return (
                i_1 != length_1 and s1[i_1] == target and dp(i_1 + 1, i_2, i_3 + 1)
            ) or (
                i_2 != length_2 and s2[i_2] == target and dp(i_1, i_2 + 1, i_3 + 1)
            )

        return dp(0, 0, 0)
