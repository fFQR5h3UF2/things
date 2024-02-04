# Submission for Soup Servings
# Submission url: https://leetcode.com/submissions/detail/1006794403/


class Solution:
    def __init__(self):
        self.moves = [[4, 0], [3, 1], [2, 2], [1, 3]]

    def soupServings(self, n: int) -> float:
        servings = n // 25
        if n % 25 != 0:
            servings += 1

        a_empty, ab_empty = self.calculate(servings, servings)
        return a_empty + ab_empty / 2

    @cache
    def calculate(self, soup_a: int, soup_b: int) -> Tuple[float, float]:

        a_empty, ab_empty = 0, 0

        for move_a, move_b in self.moves:
            new_soup_a, new_soup_b = soup_a - move_a, soup_b - move_b
            soup_a_end, soup_b_end = new_soup_a <= 0, new_soup_b <= 0

            if soup_a_end and soup_b_end:
                ab_empty += 0.25
                continue

            if soup_a_end and not soup_b_end:
                a_empty += 0.25
                continue

            if not soup_a_end and soup_b_end:
                continue

            new_a_empty, new_ab_empty = self.calculate(new_soup_a, new_soup_b)
            a_empty += 0.25 * new_a_empty
            ab_empty += 0.25 * new_ab_empty

        return a_empty, ab_empty
