# Submission title: Smallest Number in Infinite Set
# Submission url  : https://leetcode.com/problems/smallest-number-in-infinite-set/description/
# Submission url  : https://leetcode.com/submissions/detail/1052579467/
# Submission json : {"id":1052579467,"status_display":"Accepted","lang":"python3","question_id":2413,"title_slug":"smallest-number-in-infinite-set","code":"class SmallestInfiniteSet:\n\n    def __init__(self):\n        self.heap, self.next_num, self.nums = [], 1, set() \n\n\n    def popSmallest(self) -> int:\n        if not self.heap:\n            self.next_num += 1\n            return self.next_num - 1\n            \n        val = heappop(self.heap)\n        if val < self.next_num:\n            self.nums.remove(val)\n            return val\n        heappush(self.heap, val)\n        self.next_num += 1\n        return self.next_num - 1\n        \n\n    def addBack(self, num: int) -> None:\n        if num in self.nums or num >= self.next_num:\n            return\n        self.nums.add(num)\n        heappush(self.heap, num)\n\n\n# Your SmallestInfiniteSet object will be instantiated and called as such:\n# obj = SmallestInfiniteSet()\n# param_1 = obj.popSmallest()\n# obj.addBack(num)","title":"Smallest Number in Infinite Set","url":"/submissions/detail/1052579467/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695038355,"status":10,"runtime":"109 ms","is_pending":"Not Pending","memory":"16.9 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class SmallestInfiniteSet:

    def __init__(self):
        self.heap, self.next_num, self.nums = [], 1, set()

    def popSmallest(self) -> int:
        if not self.heap:
            self.next_num += 1
            return self.next_num - 1

        val = heappop(self.heap)
        if val < self.next_num:
            self.nums.remove(val)
            return val
        heappush(self.heap, val)
        self.next_num += 1
        return self.next_num - 1

    def addBack(self, num: int) -> None:
        if num in self.nums or num >= self.next_num:
            return
        self.nums.add(num)
        heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
