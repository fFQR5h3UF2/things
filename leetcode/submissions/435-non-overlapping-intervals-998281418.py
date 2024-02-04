# Submission for Non-overlapping Intervals
# Submission url: https://leetcode.com/submissions/detail/998281418/


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda element: element[1])
        length = len(intervals)
        prev, count = 0, 1

        for i in range(1, n):
            if intervals[i][0] < intervals[prev][1]:
                continue

            prev = i
            count += 1

        return length - count
