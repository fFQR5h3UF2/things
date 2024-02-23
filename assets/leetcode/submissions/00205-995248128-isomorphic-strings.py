# Submission title: Isomorphic Strings
# Submission url  : https://leetcode.com/problems/isomorphic-strings/description/
# Submission url  : https://leetcode.com/submissions/detail/995248128/"


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.index, s)) == list(map(t.index, t))
