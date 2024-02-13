# Submission title: Product of the Last K Numbers
# Submission url  : https://leetcode.com/problems/product-of-the-last-k-numbers/description/
# Submission url  : https://leetcode.com/submissions/detail/1052608131/
# Submission json : {"id":1052608131,"status_display":"Accepted","lang":"python3","question_id":1477,"title_slug":"product-of-the-last-k-numbers","code":"class ProductOfNumbers:\n\n    def __init__(self):\n        self.products = [1]\n\n    def add(self, num: int) -> None:\n        if num == 0:\n            self.products.clear()\n            self.products.append(1)\n            return\n        self.products.append(num * self.products[-1])\n\n    def getProduct(self, k: int) -> int:\n        if len(self.products) - 1 < k:\n            return 0\n        return self.products[-1] // self.products[-(k + 1)]\n\n\n# Your ProductOfNumbers object will be instantiated and called as such:\n# obj = ProductOfNumbers()\n# obj.add(num)\n# param_2 = obj.getProduct(k)","title":"Product of the Last K Numbers","url":"/submissions/detail/1052608131/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695041195,"status":10,"runtime":"218 ms","is_pending":"Not Pending","memory":"31.4 MB","compare_result":"111111111111111111111111111111111","has_notes":false,"flag_type":1}


class ProductOfNumbers:

    def __init__(self):
        self.products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.products.clear()
            self.products.append(1)
            return
        self.products.append(num * self.products[-1])

    def getProduct(self, k: int) -> int:
        if len(self.products) - 1 < k:
            return 0
        return self.products[-1] // self.products[-(k + 1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
