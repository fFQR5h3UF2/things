# Submission title: for Merge Intervals
# Submission url  : https://leetcode.com/submissions/detail/1062853417/
# Submission json : {"id": 1062853417, "status_display": "Accepted", "lang": "python3", "question_id": 56, "title_slug": "merge-intervals", "code": "class Solution:\n    def merge(self, intervals: List[List[int]]) -> List[List[int]]:\n\n        intervals.sort(key=lambda item: item[0])\n\n        merged = []\n        for start, end in intervals:\n            # if the list of merged intervals is empty or if the current\n            # interval does not overlap with the previous, simply append it.\n            if not merged or merged[-1][1] < start:\n                merged.append([start, end])\n            else:\n            # otherwise, there is overlap, so we merge the current and previous\n            # intervals.\n                merged[-1][1] = max(merged[-1][1], end)\n\n        return merged", "title": "Merge Intervals", "url": "/submissions/detail/1062853417/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1696058246, "status": 10, "runtime": "140 ms", "is_pending": "Not Pending", "memory": "21.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda item: item[0])

        merged = []
        for start, end in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], end)

        return merged
