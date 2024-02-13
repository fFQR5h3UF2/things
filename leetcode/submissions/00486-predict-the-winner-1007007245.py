# Submission title: Predict the Winner
# Submission url  : https://leetcode.com/problems/predict-the-winner/description/
# Submission url  : https://leetcode.com/submissions/detail/1007007245/
# Submission json : {"id":1007007245,"status_display":"Accepted","lang":"python3","question_id":486,"title_slug":"predict-the-winner","code":"class Solution:\n    def PredictTheWinner(self, nums: List[int]) -> bool:\n        length = len(nums)\n        is_even = length % 2 == 0\n\n        if length < 3:\n            return True\n        \n        @cache\n        def max_diff(left: int, right: int) -> int:\n            left_num, right_num = nums[left], nums[right]\n            \n            if left == right:\n                return left_num\n            \n            score_by_left = left_num - max_diff(left + 1, right)\n            score_by_right = right_num - max_diff(left, right - 1)\n            return max(score_by_left, score_by_right)\n\n        return max_diff(0, length - 1) >= 0\n","title":"Predict the Winner","url":"/submissions/detail/1007007245/","lang_name":"Python3","time":"6 months, 1 week","timestamp":1690646059,"status":10,"runtime":"37 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        length = len(nums)
        is_even = length % 2 == 0

        if length < 3:
            return True

        @cache
        def max_diff(left: int, right: int) -> int:
            left_num, right_num = nums[left], nums[right]

            if left == right:
                return left_num

            score_by_left = left_num - max_diff(left + 1, right)
            score_by_right = right_num - max_diff(left, right - 1)
            return max(score_by_left, score_by_right)

        return max_diff(0, length - 1) >= 0
