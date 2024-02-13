# Submission title: Minimum Bit Flips to Convert Number
# Submission url  : https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1056400663/
# Submission json : {"id":1056400663,"status_display":"Accepted","lang":"python3","question_id":2323,"title_slug":"minimum-bit-flips-to-convert-number","code":"class Solution:\n    def minBitFlips(self, start: int, goal: int) -> int:\n        flips_count = 0\n        while start or goal:\n            start_is_one, goal_is_one = start & 1, goal & 1\n            if start_is_one and not goal_is_one or (not start_is_one and goal_is_one):\n                flips_count += 1\n            start >>= 1\n            goal >>= 1\n        return flips_count","title":"Minimum Bit Flips to Convert Number","url":"/submissions/detail/1056400663/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695396598,"status":10,"runtime":"37 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        flips_count = 0
        while start or goal:
            start_is_one, goal_is_one = start & 1, goal & 1
            if start_is_one and not goal_is_one or (not start_is_one and goal_is_one):
                flips_count += 1
            start >>= 1
            goal >>= 1
        return flips_count
