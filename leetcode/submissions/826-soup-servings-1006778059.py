# Submission for Soup Servings
# Submission url: https://leetcode.com/submissions/detail/1006778059/


class Solution:
    def __init__(self):
        self.moves = [[-100, 0], [-75, -25], [-50, -50], [-25, -75]]

    def soupServings(self, n: int) -> float:
        a_empty, ab_empty = self.calculate(n, n)

        return a_empty + ab_empty / 2

    @cache
    def calculate(self, soup_a: int, soup_b: int) -> Tuple[float, float]:

        a_empty, ab_empty = 0, 0

        for move_a, move_b in self.moves:
            new_soup_a, new_soup_b = soup_a + move_a, soup_b + move_b

            if new_soup_a <= 0 and new_soup_b <= 0:
                ab_empty += 0.25
            elif new_soup_a <= 0:
                a_empty += 0.25
            elif new_soup_b > 0:
                new_a_empty, new_ab_empty = self.calculate(new_soup_a, new_soup_b)
                a_empty += 0.25 * new_a_empty
                ab_empty += 0.25 * new_ab_empty

        return a_empty, ab_empty
