# Submission title: Non-overlapping Intervals
# Submission url  : https://leetcode.com/problems/non-overlapping-intervals/description/
# Submission url  : https://leetcode.com/submissions/detail/998281526/
# Submission json : {"id":998281526,"status_display":"Accepted","lang":"python3","question_id":435,"title_slug":"non-overlapping-intervals","code":"class Solution:\n    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:\n        intervals = sorted(intervals, key=lambda element: element[1])\n        length = len(intervals)\n        prev, count = 0, 1\n\n        for i in range(1, length):\n            if intervals[i][0] < intervals[prev][1]:\n                continue\n            \n            prev = i\n            count += 1\n        \n        return length - count","title":"Non-overlapping Intervals","url":"/submissions/detail/998281526/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689754484,"status":10,"runtime":"1240 ms","is_pending":"Not Pending","memory":"55.3 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda element: element[1])
        length = len(intervals)
        prev, count = 0, 1

        for i in range(1, length):
            if intervals[i][0] < intervals[prev][1]:
                continue

            prev = i
            count += 1

        return length - count
