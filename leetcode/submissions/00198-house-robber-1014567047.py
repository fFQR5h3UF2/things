# Submission title: House Robber
# Submission url  : https://leetcode.com/problems/house-robber/description/
# Submission url  : https://leetcode.com/submissions/detail/1014567047/
# Submission json : {"id":1014567047,"status_display":"Accepted","lang":"python3","question_id":198,"title_slug":"house-robber","code":"class Solution:\n    def rob(self, nums: List[int]) -> int:\n        house_count = len(nums)\n        \n        @cache\n        def dp(house: int) -> int:\n            if house >= house_count:\n                return 0\n\n            return max(dp(house + 1), nums[house] + dp(house + 2)) \n\n        return dp(0)\n","title":"House Robber","url":"/submissions/detail/1014567047/","lang_name":"Python3","time":"6 months","timestamp":1691402238,"status":10,"runtime":"35 ms","is_pending":"Not Pending","memory":"16.2 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def rob(self, nums: List[int]) -> int:
        house_count = len(nums)

        @cache
        def dp(house: int) -> int:
            if house >= house_count:
                return 0

            return max(dp(house + 1), nums[house] + dp(house + 2))

        return dp(0)
