# Submission for Count Vowels Permutation
# Submission url: https://leetcode.com/submissions/detail/1086092100/


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # a -> e
        # e -> a, i
        # i -> a, e, o, u
        # o -> i, u
        # u -> a
        mod = 10**9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            a_next = e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a

            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next

        return (a + e + i + o + u) % MOD
