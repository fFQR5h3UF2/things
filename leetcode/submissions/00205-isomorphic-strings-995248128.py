# Submission title: Isomorphic Strings
# Submission url  : https://leetcode.com/problems/isomorphic-strings/description/
# Submission url  : https://leetcode.com/submissions/detail/995248128/
# Submission json : {"id":995248128,"status_display":"Accepted","lang":"python3","question_id":205,"title_slug":"isomorphic-strings","code":"class Solution:\n    def isIsomorphic(self, s: str, t: str) -> bool:\n        return list(map(s.index, s)) == list(map(t.index, t))","title":"Isomorphic Strings","url":"/submissions/detail/995248128/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689443370,"status":10,"runtime":"55 ms","is_pending":"Not Pending","memory":"17.2 MB","compare_result":"11111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return list(map(s.index, s)) == list(map(t.index, t))
