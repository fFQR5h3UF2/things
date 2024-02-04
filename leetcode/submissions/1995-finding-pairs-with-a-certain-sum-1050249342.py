# Submission for 'Finding Pairs With a Certain Sum'
# Submission url: https://leetcode.com/submissions/detail/1050249342/

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self._nums1, self._nums2, self._nums2_raw = Counter(nums1), Counter(nums2), nums2

    def add(self, index: int, val: int) -> None:
        nums2_raw, nums2 = self._nums2_raw, self._nums2
        cur_val = nums2_raw[index]
        new_val = cur_val + val
        if nums2[cur_val] > 0:
            nums2[cur_val] -= 1

        nums2_raw[index] = new_val
        nums2[new_val] += 1

    def count(self, tot: int) -> int:
        return sum(num1_count * self._nums2.get(tot - num1, 0)
                   for num1, num1_count in self._nums1.items())


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
