# Submission for Count All Valid Pickup and Delivery Options
# Submission url: https://leetcode.com/submissions/detail/1045511473/


class Solution:
    def countOrders(self, n: int) -> int:

        pickup, delivery = set(), set()

        def backtrack() -> int:
            if len(pickup) == len(delivery) == n:
                return 1

            ways_count = 0

            for i in range(n):
                is_picked, is_delivered = i in pickup, i in delivery
                if not is_picked and not is_delivered:
                    pickup.add(i)
                    ways_count += backtrack()
                    pickup.remove(i)

                if is_picked and not is_delivered:
                    delivery.add(i)
                    ways_count += backtrack()
                    delivery.remove(i)

            return ways_count

        return backtrack()
