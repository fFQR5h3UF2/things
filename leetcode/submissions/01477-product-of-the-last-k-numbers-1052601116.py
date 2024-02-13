# Submission title: Product of the Last K Numbers
# Submission url  : https://leetcode.com/problems/product-of-the-last-k-numbers/description/
# Submission url  : https://leetcode.com/submissions/detail/1052601116/
# Submission json : {"id":1052601116,"status_display":"Accepted","lang":"python3","question_id":1477,"title_slug":"product-of-the-last-k-numbers","code":"class ProductOfNumbers:\n\n    def __init__(self):\n        self.products, self.zero_indexes = [], []\n\n    def add(self, num: int) -> None:\n        if num == 0:\n            self.zero_indexes.append(len(self.products))\n            num = 1\n        new_product = num * (self.products[-1] if self.products else 1)\n        self.products.append(new_product)\n\n    def getProduct(self, k: int) -> int:\n        first_elem = len(self.products) - k\n        if self.zero_indexes and self.zero_indexes[-1] >= first_elem:\n            return 0\n        if first_elem == 0:\n            return self.products[-1]\n        return self.products[-1] // self.products[first_elem - 1]\n\n\n# Your ProductOfNumbers object will be instantiated and called as such:\n# obj = ProductOfNumbers()\n# obj.add(num)\n# param_2 = obj.getProduct(k)","title":"Product of the Last K Numbers","url":"/submissions/detail/1052601116/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695040546,"status":10,"runtime":"269 ms","is_pending":"Not Pending","memory":"165.8 MB","compare_result":"111111111111111111111111111111111","has_notes":false,"flag_type":1}


class ProductOfNumbers:

    def __init__(self):
        self.products, self.zero_indexes = [], []

    def add(self, num: int) -> None:
        if num == 0:
            self.zero_indexes.append(len(self.products))
            num = 1
        new_product = num * (self.products[-1] if self.products else 1)
        self.products.append(new_product)

    def getProduct(self, k: int) -> int:
        first_elem = len(self.products) - k
        if self.zero_indexes and self.zero_indexes[-1] >= first_elem:
            return 0
        if first_elem == 0:
            return self.products[-1]
        return self.products[-1] // self.products[first_elem - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
