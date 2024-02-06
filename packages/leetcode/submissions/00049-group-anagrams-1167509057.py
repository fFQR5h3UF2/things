# Submission title: for Group Anagrams
# Submission url  : https://leetcode.com/submissions/detail/1167509057/
# Submission json : {"id": 1167509057, "status_display": "Accepted", "lang": "python3", "question_id": 49, "title_slug": "group-anagrams", "code": "class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        anagrams = defaultdict(list)\n        for anagram in strs:\n            anagrams[tuple(sorted(anagram))].append(anagram)\n        return anagrams.values()", "title": "Group Anagrams", "url": "/submissions/detail/1167509057/", "lang_name": "Python3", "time": "0\u00a0minutes", "timestamp": 1707199371, "status": 10, "runtime": "76 ms", "is_pending": "Not Pending", "memory": "20.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for anagram in strs:
            anagrams[tuple(sorted(anagram))].append(anagram)
        return anagrams.values()
