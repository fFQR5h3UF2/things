# Submission title: Unique Number of Occurrences
# Submission url  : https://leetcode.com/problems/unique-number-of-occurrences/description/
# Submission url  : https://leetcode.com/submissions/detail/1148942931/
# Submission json : {"id":1148942931,"status_display":"Accepted","lang":"python3","question_id":1319,"title_slug":"unique-number-of-occurrences","code":"class Solution:\n    def uniqueOccurrences(self, arr: List[int]) -> bool:\n        counts = defaultdict(int)\n        for num in arr:\n            counts[num] += 1\n\n        viewed = set()\n        for _, count in counts.items():\n            if count in viewed:\n                return False\n            viewed.add(count)\n        return True","title":"Unique Number of Occurrences","url":"/submissions/detail/1148942931/","lang_name":"Python3","time":"2 weeks, 3 days","timestamp":1705508044,"status":10,"runtime":"31 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for num in arr:
            counts[num] += 1

        viewed = set()
        for _, count in counts.items():
            if count in viewed:
                return False
            viewed.add(count)
        return True
