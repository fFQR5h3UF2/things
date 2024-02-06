# Submission title: for Group Anagrams
# Submission url  : https://leetcode.com/submissions/detail/997525401/
# Submission json : {"id": 997525401, "status_display": "Accepted", "lang": "python3", "question_id": 49, "title_slug": "group-anagrams", "code": "class Solution:\n    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:\n        anagrams: Dict[str, List[str]] = defaultdict(list)\n\n        for string in strs:\n            anagrams[\"\".join(sorted(string))].append(string)\n        \n        return anagrams.values()\n\n", "title": "Group Anagrams", "url": "/submissions/detail/997525401/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689681196, "status": 10, "runtime": "108 ms", "is_pending": "Not Pending", "memory": "20.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams: Dict[str, List[str]] = defaultdict(list)

        for string in strs:
            anagrams["".join(sorted(string))].append(string)

        return anagrams.values()
