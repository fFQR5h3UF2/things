# Submission for Finding Pairs With a Certain Sum
# Submission url: https://leetcode.com/submissions/detail/1050240620/


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self._nums2 = nums2
        self._nums1 = Counter(nums1)

    def add(self, index: int, val: int) -> None:
        self._nums2[index] += val

    def count(self, tot: int) -> int:
        count = 0
        for num in self._nums2:
            count += self._nums1.get(tot - num, 0)

        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
