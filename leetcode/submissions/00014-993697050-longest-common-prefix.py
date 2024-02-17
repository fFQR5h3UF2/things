# Submission title: Longest Common Prefix
# Submission url  : https://leetcode.com/problems/longest-common-prefix/description/"
# Submission url  : https://leetcode.com/submissions/detail/993697050/"


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        min_length = min([len(string) for string in strs])
        prefix = strs[0][0:min_length]
        for string in strs:
            if not prefix:
                return ""

            while not string.startswith(prefix):
                prefix = prefix[0:-1]

        return prefix
