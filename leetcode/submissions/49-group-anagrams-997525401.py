# Submission for 'Group Anagrams'
# Submission url: https://leetcode.com/submissions/detail/997525401/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str, List[str]] = defaultdict(list)

        for string in strs:
            anagrams["".join(sorted(string))].append(string)

        return anagrams.values()
