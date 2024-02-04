# Submission for Apply Discount Every n Orders
# Submission url: https://leetcode.com/submissions/detail/1051152086/


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.products, self.prices = products, prices
        self.freq, self.discount = n, (100 - discount) / 100
        self.cur = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cur += 1
        multiplier = 1
        if self.cur == self.freq:
            self.cur = 0
            multiplier = self.discount
        total = sum(
            amount[i] * self.prices[product[i] - 1] for i in range(len(product))
        )
        return total * multiplier


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
