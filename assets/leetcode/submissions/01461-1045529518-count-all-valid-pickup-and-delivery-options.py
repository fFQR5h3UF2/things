# Submission title: Count All Valid Pickup and Delivery Options
# Submission url  : https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
# Submission url  : https://leetcode.com/submissions/detail/1045529518/"


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
            ways_count *= sum(
                avail_pos_count - pos for pos in range(avail_pos_count)
            )

        return ways_count % (10**9 + 7)
