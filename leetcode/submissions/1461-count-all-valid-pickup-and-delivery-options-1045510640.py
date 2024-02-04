# Submission for Count All Valid Pickup and Delivery Options
# Submission url: https://leetcode.com/submissions/detail/1045510640/


class Solution:
    def countOrders(self, n: int) -> int:

        pickup, delivery = set(), set()

        def backtrack() -> int:
            if len(pickup) == len(delivery) == n:
                return 1

            ways_count = 0

            for i in range(n):
                if i not in pickup:
                    pickup.add(i)
                    ways_count += backtrack()
                    pickup.remove(i)

                if i not in delivery:
                    delivery.add(i)
                    ways_count += backtrack()
                    delivery.remove(i)

            return ways_count

        return backtrack()
