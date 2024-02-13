# Submission title: Count Vowels Permutation
# Submission url  : https://leetcode.com/problems/count-vowels-permutation/description/
# Submission url  : https://leetcode.com/submissions/detail/1086092477/
# Submission json : {"id":1086092477,"status_display":"Accepted","lang":"python3","question_id":1332,"title_slug":"count-vowels-permutation","code":"class Solution:\n    def countVowelPermutation(self, n: int) -> int:\n        MOD = 10**9 + 7\n        \n        a, e, i, o, u = 1, 1, 1, 1, 1\n        \n        for _ in range(1, n):\n            a_next = e\n            e_next = (a + i) % MOD\n            i_next = (a + e + o + u) % MOD\n            o_next = (i + u) % MOD\n            u_next = a\n            \n            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next\n        \n        return (a + e + i + o + u) % MOD","title":"Count Vowels Permutation","url":"/submissions/detail/1086092477/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698504664,"status":10,"runtime":"84 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"1111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7

        a, e, i, o, u = 1, 1, 1, 1, 1

        for _ in range(1, n):
            a_next = e
            e_next = (a + i) % MOD
            i_next = (a + e + o + u) % MOD
            o_next = (i + u) % MOD
            u_next = a

            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next

        return (a + e + i + o + u) % MOD
