# Submission title: Minimum Number of Taps to Open to Water a Garden
# Submission url  : https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/
# Submission url  : https://leetcode.com/submissions/detail/1036676232/
# Submission json : {"id":1036676232,"status_display":"Accepted","lang":"python3","question_id":1451,"title_slug":"minimum-number-of-taps-to-open-to-water-a-garden","code":"class Solution:\n    def minTaps(self, n: int, ranges: List[int]) -> int:\n        arr = [0] * (n + 1)\n        for i, r in enumerate(ranges):\n            if r == 0:\n                continue\n            left = max(0, i - r)\n            arr[left] = max(arr[left], i + r)\n\n        end, far_can_reach, cnt = 0, 0, 0\n        \n        for i, reach in enumerate(arr):\n            if i > end:\n                if far_can_reach <= end:\n                    return -1\n                end, cnt = far_can_reach, cnt + 1\n            far_can_reach = max(far_can_reach, reach)\n\n        return cnt + (end < n)\n","title":"Minimum Number of Taps to Open to Water a Garden","url":"/submissions/detail/1036676232/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693473280,"status":10,"runtime":"116 ms","is_pending":"Not Pending","memory":"16.9 MB","compare_result":"11111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n + 1)
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            left = max(0, i - r)
            arr[left] = max(arr[left], i + r)

        end, far_can_reach, cnt = 0, 0, 0

        for i, reach in enumerate(arr):
            if i > end:
                if far_can_reach <= end:
                    return -1
                end, cnt = far_can_reach, cnt + 1
            far_can_reach = max(far_can_reach, reach)

        return cnt + (end < n)
