# Submission for Find Median from Data Stream
# Submission url: https://leetcode.com/submissions/detail/1057879315/


class MedianFinder:

    def __init__(self):
        self.nums = []
        self.med = -1
        self.even = True

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.even = not self.even
        half = len(self.nums) // 2
        if self.even:
            self.med = (self.nums[half] + self.nums[half - 1]) / 2
        else:
            self.med = self.nums[half]

    def findMedian(self) -> float:
        return self.med


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
