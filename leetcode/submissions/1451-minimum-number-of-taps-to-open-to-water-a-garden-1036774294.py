# Submission for Minimum Number of Taps to Open to Water a Garden
# Submission url: https://leetcode.com/submissions/detail/1036774294/


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        taps_to_remove = []

        for tap in range(n + 1):
            tap_range = ranges[tap]
            if tap_range == 0:
                taps_to_remove.append(tap)
                continue

            start, end = tap - tap_range, tap + tap_range
            if start <= 0 and end >= n:
                return 1

            ranges[tap] = (start, end)

        for tap_to_remove in reversed(taps_to_remove):
            ranges[tap_to_remove] = ranges[-1]
            ranges.pop()

        taps_count = len(ranges)
        if taps_count == 0:
            return -1

        ranges.sort()

        @cache
        def dp(i: int, covered: int, curr_tap: int) -> int:
            if i == n:
                return 0

            min_taps = dp(i + 1, covered, curr_tap) if i < covered else -1

            for start, end in ranges[curr_tap:taps_count]:
                if not start <= i <= end:
                    continue

                taps = 1 + dp(i + 1, end, curr_tap + 1)
                if taps == 0:
                    continue

                if min_taps == -1 or taps < min_taps:
                    min_taps = taps

            return min_taps

        return dp(0, 0, 0)
