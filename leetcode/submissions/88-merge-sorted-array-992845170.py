# Submission for Merge Sorted Array
# Submission url: https://leetcode.com/submissions/detail/992845170/


class Solution:
    # if the last nums2 number is smaller than the first nums1 number, we just need to
    # put nums2 + nums1
    # if the last nums1 number is smaller than the first nums2 number, we just need to
    # put nums1 + nums2
    # iterate over nums2 from the end
    # if number is bigger than the last nums1 number, insert to the end
    # if number is smaller than the last nums1 number, insert the last nums1 one number
    # to the end together with other nums1 numbers that are less than the nums2 number
    #
    # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    # nums1 = [1,2,3,2,5,6]
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        left, right = m - 1 if m else 0, m + n - 1

        while left >= 0 and left <= right:
            if right >= m:
                nums1[right] = nums2[right - m]

            left_number, right_number = nums1[left], nums1[right]

            if right_number >= left_number:
                right -= 1
                continue

            nums1[left], nums1[right] = right_number, left_number
            right -= 1
            if left != 0:
                left -= 1
