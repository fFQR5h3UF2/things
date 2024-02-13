# Submission title: Design Bitset
# Submission url  : https://leetcode.com/problems/design-bitset/description/
# Submission url  : https://leetcode.com/submissions/detail/1053831460/
# Submission json : {"id":1053831460,"status_display":"Accepted","lang":"python3","question_id":2285,"title_slug":"design-bitset","code":"class Bitset:\n\n    def __init__(self, size: int):\n        self.bits = [0] * size\n        self.ones_count = 0\n        self.do_flip = False\n        self.size = size\n\n    def fix(self, idx: int) -> None:\n        cur = self.bits[idx]\n        if self.do_flip and cur == 1:\n            self.ones_count -= 1\n            self.bits[idx] = 0\n        elif not self.do_flip and cur == 0:\n            self.ones_count += 1\n            self.bits[idx] = 1\n\n    def unfix(self, idx: int) -> None:\n        cur = self.bits[idx]\n        if self.do_flip and cur == 0:\n            self.ones_count += 1\n            self.bits[idx] = 1\n        elif not self.do_flip and cur == 1:\n            self.ones_count -= 1\n            self.bits[idx] = 0\n\n    def flip(self) -> None:\n        self.do_flip = not self.do_flip\n\n    def all(self) -> bool:\n        return self.count() == self.size\n\n    def one(self) -> bool:\n        return self.count() > 0\n\n    def count(self) -> int:\n        return self.size - self.ones_count if self.do_flip else self.ones_count\n\n    def toString(self) -> str:\n        target = (bit ^ 1 for bit in self.bits) if self.do_flip else self.bits\n        return \"\".join(str(num) for num in target)\n\n\n# Your Bitset object will be instantiated and called as such:\n# obj = Bitset(size)\n# obj.fix(idx)\n# obj.unfix(idx)\n# obj.flip()\n# param_4 = obj.all()\n# param_5 = obj.one()\n# param_6 = obj.count()\n# param_7 = obj.toString()","title":"Design Bitset","url":"/submissions/detail/1053831460/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695146896,"status":10,"runtime":"605 ms","is_pending":"Not Pending","memory":"47.6 MB","compare_result":"111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Bitset:

    def __init__(self, size: int):
        self.bits = [0] * size
        self.ones_count = 0
        self.do_flip = False
        self.size = size

    def fix(self, idx: int) -> None:
        cur = self.bits[idx]
        if self.do_flip and cur == 1:
            self.ones_count -= 1
            self.bits[idx] = 0
        elif not self.do_flip and cur == 0:
            self.ones_count += 1
            self.bits[idx] = 1

    def unfix(self, idx: int) -> None:
        cur = self.bits[idx]
        if self.do_flip and cur == 0:
            self.ones_count += 1
            self.bits[idx] = 1
        elif not self.do_flip and cur == 1:
            self.ones_count -= 1
            self.bits[idx] = 0

    def flip(self) -> None:
        self.do_flip = not self.do_flip

    def all(self) -> bool:
        return self.count() == self.size

    def one(self) -> bool:
        return self.count() > 0

    def count(self) -> int:
        return self.size - self.ones_count if self.do_flip else self.ones_count

    def toString(self) -> str:
        target = (bit ^ 1 for bit in self.bits) if self.do_flip else self.bits
        return "".join(str(num) for num in target)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
