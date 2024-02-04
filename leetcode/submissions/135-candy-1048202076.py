# Submission for Candy
# Submission url: https://leetcode.com/submissions/detail/1048202076/


class Solution:
    def candy(self, ratings: List[int]) -> int:
        child_count = len(ratings)
        candies = [1] * child_count

        for i in range(child_count - 1):
            cur_rat, next_rat = ratings[i], ratings[i + 1]
            cur_can, next_can = candies[i], candies[i + 1]

            if cur_rat > next_rat and cur_can <= next_can:
                candies[i] = next_can + 1
            elif cur_rat < next_rat and cur_can >= next_can:
                candies[i + 1] = cur_can + 1

        return sum(candies)
