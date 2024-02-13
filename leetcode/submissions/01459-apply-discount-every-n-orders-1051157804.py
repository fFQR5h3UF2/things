# Submission title: Apply Discount Every n Orders
# Submission url  : https://leetcode.com/problems/apply-discount-every-n-orders/description/
# Submission url  : https://leetcode.com/submissions/detail/1051157804/
# Submission json : {"id":1051157804,"status_display":"Accepted","lang":"python3","question_id":1459,"title_slug":"apply-discount-every-n-orders","code":"class Cashier:\n\n    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):\n        self.freq, self.discount = n, (100 - discount) / 100\n        self.cur = 0\n        self.products = {id: price for id, price in zip(products, prices)}\n\n    def getBill(self, product: List[int], amount: List[int]) -> float:\n        self.cur += 1\n        total = sum(amount[i] * self.products[product[i]] for i in range(len(product)))\n        if self.cur < self.freq:\n            return total\n        self.cur = 0\n        return total * self.discount\n        \n\n\n# Your Cashier object will be instantiated and called as such:\n# obj = Cashier(n, discount, products, prices)\n# param_1 = obj.getBill(product,amount)","title":"Apply Discount Every n Orders","url":"/submissions/detail/1051157804/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1694887805,"status":10,"runtime":"1201 ms","is_pending":"Not Pending","memory":"24.8 MB","compare_result":"1111111111111111111111111","has_notes":false,"flag_type":1}


class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.freq, self.discount = n, (100 - discount) / 100
        self.cur = 0
        self.products = {id: price for id, price in zip(products, prices)}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.cur += 1
        total = sum(amount[i] * self.products[product[i]] for i in range(len(product)))
        if self.cur < self.freq:
            return total
        self.cur = 0
        return total * self.discount


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
