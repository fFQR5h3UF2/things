# Submission for Smallest Number in Infinite Set
# Submission url: https://leetcode.com/submissions/detail/1052574465/


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        heappush(self.heap, 1)
        self.cur = 2
        self.nums = set((1,))

    def popSmallest(self) -> int:
        if self.heap:
            val = heappop(self.heap)
            self.nums.remove(val)
            return val

        smallest = self.cur
        self.cur += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.nums:
            return
        self.nums.add(num)
        heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
