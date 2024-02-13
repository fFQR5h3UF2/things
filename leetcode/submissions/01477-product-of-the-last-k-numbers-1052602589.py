# Submission title: Product of the Last K Numbers
# Submission url  : https://leetcode.com/problems/product-of-the-last-k-numbers/description/
# Submission url  : https://leetcode.com/submissions/detail/1052602589/
# Submission json : {"id":1052602589,"status_display":"Accepted","lang":"python3","question_id":1477,"title_slug":"product-of-the-last-k-numbers","code":"class ProductOfNumbers:\n\n    def __init__(self):\n        self.products, self.last_zero, self.length = [], -1, 0\n\n    def add(self, num: int) -> None:\n        if num == 0:\n            self.last_zero = self.length\n            num = 1\n        self.products.append(num * (self.products[-1] if self.products else 1))\n        self.length += 1\n\n    def getProduct(self, k: int) -> int:\n        first_elem = self.length - k\n        if self.last_zero >= first_elem:\n            return 0\n        if first_elem == 0:\n            return self.products[-1]\n        return self.products[-1] // self.products[first_elem - 1]\n\n\n# Your ProductOfNumbers object will be instantiated and called as such:\n# obj = ProductOfNumbers()\n# obj.add(num)\n# param_2 = obj.getProduct(k)","title":"Product of the Last K Numbers","url":"/submissions/detail/1052602589/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695040684,"status":10,"runtime":"235 ms","is_pending":"Not Pending","memory":"165.6 MB","compare_result":"111111111111111111111111111111111","has_notes":false,"flag_type":1}


class ProductOfNumbers:

    def __init__(self):
        self.products, self.last_zero, self.length = [], -1, 0

    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = self.length
            num = 1
        self.products.append(num * (self.products[-1] if self.products else 1))
        self.length += 1

    def getProduct(self, k: int) -> int:
        first_elem = self.length - k
        if self.last_zero >= first_elem:
            return 0
        if first_elem == 0:
            return self.products[-1]
        return self.products[-1] // self.products[first_elem - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
