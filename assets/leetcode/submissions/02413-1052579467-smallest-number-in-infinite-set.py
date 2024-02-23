# Submission title: Smallest Number in Infinite Set
# Submission url  : https://leetcode.com/problems/smallest-number-in-infinite-set/description/
# Submission url  : https://leetcode.com/submissions/detail/1052579467/"


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
