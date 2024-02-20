# Submission title: Group Anagrams
# Submission url  : https://leetcode.com/problems/group-anagrams/description/
# Submission url  : https://leetcode.com/submissions/detail/1167509057/"


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for anagram in strs:
            anagrams[tuple(sorted(anagram))].append(anagram)
        return anagrams.values()
