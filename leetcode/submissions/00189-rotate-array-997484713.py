# Submission title: Rotate Array
# Submission url  : https://leetcode.com/problems/rotate-array/description/
# Submission url  : https://leetcode.com/submissions/detail/997484713/
# Submission json : {"id":997484713,"status_display":"Accepted","lang":"python3","question_id":189,"title_slug":"rotate-array","code":"class Solution:\n    def rotate(self, nums: List[int], k: int) -> None:\n        \"\"\"\n        Do not return anything, modify nums in-place instead.\n        \"\"\"\n        length = len(nums)\n        k %= length\n        nums[length - k:] = nums[length - k:][::-1]  \n        nums[:length - k] = nums[:length - k][::-1]   \n        nums[:] = nums[::-1] \n","title":"Rotate Array","url":"/submissions/detail/997484713/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689677300,"status":10,"runtime":"230 ms","is_pending":"Not Pending","memory":"27.7 MB","compare_result":"11111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k %= length
        nums[length - k :] = nums[length - k :][::-1]
        nums[: length - k] = nums[: length - k][::-1]
        nums[:] = nums[::-1]
