# Submission title: Sort Characters By Frequency
# Submission url  : https://leetcode.com/problems/sort-characters-by-frequency/description/
# Submission url  : https://leetcode.com/submissions/detail/1168581047/
# Submission json : {"id":1168581047,"status_display":"Accepted","lang":"python3","question_id":451,"title_slug":"sort-characters-by-frequency","code":"class Solution:\n    def frequencySort(self, s: str) -> str:\n        counter = defaultdict(int)\n        for char in s:\n            counter[char] += 1\n        return \"\".join(sorted(s, key=lambda val: -(ord(val) + counter[val] * 100)))","title":"Sort Characters By Frequency","url":"/submissions/detail/1168581047/","lang_name":"Python3","time":"37 minutes","timestamp":1707292147,"status":10,"runtime":"80 ms","is_pending":"Not Pending","memory":"23.3 MB","compare_result":"111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        return "".join(sorted(s, key=lambda val: -(ord(val) + counter[val] * 100)))
