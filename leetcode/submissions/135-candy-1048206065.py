# Submission for Candy
# Submission url: https://leetcode.com/submissions/detail/1048206065/


class Solution:
    def candy(self, ratings: List[int]) -> int:
        child_count = len(ratings)
        candies = [1] * child_count
        start_index = 0
        while True:
            try_again = False

            for i in range(start_index, child_count - 1):
                cur_rat, next_rat = ratings[i], ratings[i + 1]
                cur_can, next_can = candies[i], candies[i + 1]

                if cur_rat > next_rat and cur_can <= next_can:
                    candies[i] = next_can + 1
                    start_index = min(start_index, i)
                    try_again = True
                elif cur_rat < next_rat and cur_can >= next_can:
                    candies[i + 1] = cur_can + 1
                    start_index = min(start_index, i)
                    try_again = True

            if not try_again:
                break

        return sum(candies)
