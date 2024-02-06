# Submission title: for Finding Pairs With a Certain Sum
# Submission url  : https://leetcode.com/submissions/detail/1050249342/
# Submission json : {"id": 1050249342, "status_display": "Accepted", "lang": "python3", "question_id": 1995, "title_slug": "finding-pairs-with-a-certain-sum", "code": "class FindSumPairs:\n\n    def __init__(self, nums1: List[int], nums2: List[int]):\n        self._nums1, self._nums2, self._nums2_raw = Counter(nums1), Counter(nums2), nums2\n\n    def add(self, index: int, val: int) -> None:\n        nums2_raw, nums2 = self._nums2_raw, self._nums2\n        cur_val = nums2_raw[index]\n        new_val = cur_val + val\n        if nums2[cur_val] > 0:\n            nums2[cur_val] -= 1\n        \n        nums2_raw[index] = new_val\n        nums2[new_val] += 1\n\n    def count(self, tot: int) -> int:       \n        return sum(num1_count * self._nums2.get(tot - num1, 0) \n                   for num1, num1_count in self._nums1.items())\n\n\n# Your FindSumPairs object will be instantiated and called as such:\n# obj = FindSumPairs(nums1, nums2)\n# obj.add(index,val)\n# param_2 = obj.count(tot)", "title": "Finding Pairs With a Certain Sum", "url": "/submissions/detail/1050249342/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694795684, "status": 10, "runtime": "596 ms", "is_pending": "Not Pending", "memory": "48.8 MB", "compare_result": "11111111111111111111111111", "has_notes": false, "flag_type": 1}


class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self._nums1, self._nums2, self._nums2_raw = (
            Counter(nums1),
            Counter(nums2),
            nums2,
        )

    def add(self, index: int, val: int) -> None:
        nums2_raw, nums2 = self._nums2_raw, self._nums2
        cur_val = nums2_raw[index]
        new_val = cur_val + val
        if nums2[cur_val] > 0:
            nums2[cur_val] -= 1

        nums2_raw[index] = new_val
        nums2[new_val] += 1

    def count(self, tot: int) -> int:
        return sum(
            num1_count * self._nums2.get(tot - num1, 0)
            for num1, num1_count in self._nums1.items()
        )


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
