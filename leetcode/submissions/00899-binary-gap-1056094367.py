# Submission title: Binary Gap
# Submission url  : https://leetcode.com/problems/binary-gap/description/
# Submission url  : https://leetcode.com/submissions/detail/1056094367/
# Submission json : {"id":1056094367,"status_display":"Accepted","lang":"python3","question_id":899,"title_slug":"binary-gap","code":"class Solution:\n    def binaryGap(self, n: int) -> int:\n        i, first_bit = 0, None\n        max_distance = 0\n        while n:\n            is_one = n & 1 == 1\n            if is_one and first_bit is None:\n                first_bit = i\n            elif is_one:\n                max_distance, first_bit = max(max_distance, i - first_bit), i\n            n >>= 1\n            i += 1\n        \n        return max_distance ","title":"Binary Gap","url":"/submissions/detail/1056094367/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695367478,"status":10,"runtime":"45 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def binaryGap(self, n: int) -> int:
        i, first_bit = 0, None
        max_distance = 0
        while n:
            is_one = n & 1 == 1
            if is_one and first_bit is None:
                first_bit = i
            elif is_one:
                max_distance, first_bit = max(max_distance, i - first_bit), i
            n >>= 1
            i += 1

        return max_distance
