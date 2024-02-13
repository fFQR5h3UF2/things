# Submission title: Single Number II
# Submission url  : https://leetcode.com/problems/single-number-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1057807079/
# Submission json : {"id":1057807079,"status_display":"Accepted","lang":"python3","question_id":137,"title_slug":"single-number-ii","code":"class Solution:\n    def singleNumber(self, nums: List[int]) -> int:\n        nums.sort()\n        length = len(nums)\n        for i in range(0, length, 3):\n            if i == length - 1:\n                return nums[i]\n    \n            num_1, num_2, num_3 = nums[i], nums[i+1], nums[i+2]\n\n            if num_1 == num_2 == num_3:\n                continue\n            \n            if num_2 == num_3:\n                return num_1\n            \n            if num_1 == num_3:\n                return num_2\n            \n            return num_3\n            ","title":"Single Number II","url":"/submissions/detail/1057807079/","lang_name":"Python3","time":"4 months, 1 week","timestamp":1695549154,"status":10,"runtime":"61 ms","is_pending":"Not Pending","memory":"17.9 MB","compare_result":"11111111111111","has_notes":false,"flag_type":1}


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)
        for i in range(0, length, 3):
            if i == length - 1:
                return nums[i]

            num_1, num_2, num_3 = nums[i], nums[i + 1], nums[i + 2]

            if num_1 == num_2 == num_3:
                continue

            if num_2 == num_3:
                return num_1

            if num_1 == num_3:
                return num_2

            return num_3
