# Submission title: Jump Game
# Submission url  : https://leetcode.com/problems/jump-game/description/
# Submission url  : https://leetcode.com/submissions/detail/998293324/
# Submission json : {"id":998293324,"status_display":"Accepted","lang":"python3","question_id":55,"title_slug":"jump-game","code":"class Solution:\n    def canJump(self, nums: List[int]) -> bool:\n        length = len(nums)\n\n        if length < 2:\n            return True\n        \n        current = nums[0]\n\n        for i in range(1, length):\n            if current == 0:\n                return False\n            current -= 1\n            current = max(current, nums[i])\n        \n        return True\n            ","title":"Jump Game","url":"/submissions/detail/998293324/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689755656,"status":10,"runtime":"553 ms","is_pending":"Not Pending","memory":"17.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)

        if length < 2:
            return True

        current = nums[0]

        for i in range(1, length):
            if current == 0:
                return False
            current -= 1
            current = max(current, nums[i])

        return True
