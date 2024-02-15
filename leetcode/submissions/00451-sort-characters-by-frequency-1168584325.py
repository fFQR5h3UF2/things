# Submission title: Sort Characters By Frequency
# Submission url  : https://leetcode.com/problems/sort-characters-by-frequency/description/
# Submission url  : https://leetcode.com/submissions/detail/1168584325/
# Submission json : {"id":1168584325,"status_display":"Accepted","lang":"python3","question_id":451,"title_slug":"sort-characters-by-frequency","code":"class Solution:\n    def frequencySort(self, s: str) -> str:\n        counter = {}\n        for char in s:\n            if char not in counter:\n                counter[char] = -ord(char)\n            counter[char] -= 100\n        return \"\".join(sorted(s, key=lambda val: counter[val]))","title":"Sort Characters By Frequency","url":"/submissions/detail/1168584325/","lang_name":"Python3","time":"32 minutes","timestamp":1707292460,"status":10,"runtime":"67 ms","is_pending":"Not Pending","memory":"19.3 MB","compare_result":"111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = -ord(char)
            counter[char] -= 100
        return "".join(sorted(s, key=lambda val: counter[val]))