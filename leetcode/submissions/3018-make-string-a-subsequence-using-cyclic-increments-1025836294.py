# Submission for Make String a Subsequence Using Cyclic Increments
# Submission url: https://leetcode.com/submissions/detail/1025836294/


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        length1, length2 = len(str1), len(str2)

        for i in range(length1):
            if i + length2 > length1:
                break

            str2_i = 0
            for j in range(i, length1):
                if ord(str2[str2_i]) - ord(str1[j]) in (0, 1, -25):
                    str2_i += 1
                    continue

            if str2_i == length2:
                return True

        return False
