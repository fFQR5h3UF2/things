# Submission title: Element Appearing More Than 25% In Sorted Array
# Submission url  : https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1117030857/"


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        prev, count = arr[0], 1
        quarter = len(arr) / 4
        for num in arr[1:]:
            if num == prev:
                count += 1
            else:
                prev = num
                count = 1
            if count > quarter:
                break
        return prev
