# Submission title: Count All Valid Pickup and Delivery Options
# Submission url  : https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
# Submission url  : https://leetcode.com/submissions/detail/1045529518/
# Submission json : {"id":1045529518,"status_display":"Accepted","lang":"python3","question_id":1461,"title_slug":"count-all-valid-pickup-and-delivery-options","code":"class Solution:\n    def countOrders(self, n: int) -> int:\n        # P1, D1                 [01] -> (P1, D1)\n        # P1, D1, P2, D2         [06] -> (P1, P2, D1, D2), (P1, P2, D2, D1), \n        #                                (P1, D1, P2, D2), (P2, P1, D1, D2), \n        #                                (P2, P1, D2, D1), (P2, D2, P1, D1).\n        # P1, D1, P2, D2, P3, D3 [90]\n        \n        ways_count = 1\n        for order in range(2, n + 1):\n            avail_pos_count = 1 + (order - 1) * 2\n            ways_count *= sum(avail_pos_count - pos for pos in range(avail_pos_count))\n\n        return ways_count % (10**9 + 7)","title":"Count All Valid Pickup and Delivery Options","url":"/submissions/detail/1045529518/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694338658,"status":10,"runtime":"120 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def countOrders(self, n: int) -> int:
        # P1, D1                 [01] -> (P1, D1)
        # P1, D1, P2, D2         [06] -> (P1, P2, D1, D2), (P1, P2, D2, D1),
        #                                (P1, D1, P2, D2), (P2, P1, D1, D2),
        #                                (P2, P1, D2, D1), (P2, D2, P1, D1).
        # P1, D1, P2, D2, P3, D3 [90]

        ways_count = 1
        for order in range(2, n + 1):
            avail_pos_count = 1 + (order - 1) * 2
            ways_count *= sum(avail_pos_count - pos for pos in range(avail_pos_count))

        return ways_count % (10**9 + 7)
