# Submission title: Count All Valid Pickup and Delivery Options
# Submission url  : https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
# Submission url  : https://leetcode.com/submissions/detail/1045535680/
# Submission json : {"id":1045535680,"status_display":"Accepted","lang":"python3","question_id":1461,"title_slug":"count-all-valid-pickup-and-delivery-options","code":"class Solution:\n    def countOrders(self, n: int) -> int:\n        # P1, D1                 [01] -> (P1, D1)\n        # P1, D1, P2, D2         [06] -> (P1, P2, D1, D2), (P1, P2, D2, D1), \n        #                                (P1, D1, P2, D2), (P2, P1, D1, D2), \n        #                                (P2, P1, D2, D1), (P2, D2, P1, D1).\n        # P1, D1, P2, D2, P3, D3 [90]\n        \n        ways_count = 1\n        mod = 10**9 + 7\n        for order in range(2, n + 1):\n            pos_avail_count = 1 + (order - 1) * 2\n            cur_ways_count = pos_avail_count * (pos_avail_count + 1) // 2\n            ways_count = (ways_count * cur_ways_count) % mod\n\n        return ways_count","title":"Count All Valid Pickup and Delivery Options","url":"/submissions/detail/1045535680/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694339294,"status":10,"runtime":"44 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def countOrders(self, n: int) -> int:
        # P1, D1                 [01] -> (P1, D1)
        # P1, D1, P2, D2         [06] -> (P1, P2, D1, D2), (P1, P2, D2, D1),
        #                                (P1, D1, P2, D2), (P2, P1, D1, D2),
        #                                (P2, P1, D2, D1), (P2, D2, P1, D1).
        # P1, D1, P2, D2, P3, D3 [90]

        ways_count = 1
        mod = 10**9 + 7
        for order in range(2, n + 1):
            pos_avail_count = 1 + (order - 1) * 2
            cur_ways_count = pos_avail_count * (pos_avail_count + 1) // 2
            ways_count = (ways_count * cur_ways_count) % mod

        return ways_count
