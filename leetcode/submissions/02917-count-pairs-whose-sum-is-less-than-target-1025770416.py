# Submission title: Count Pairs Whose Sum is Less than Target
# Submission url  : https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/
# Submission url  : https://leetcode.com/submissions/detail/1025770416/
# Submission json : {"id":1025770416,"status_display":"Accepted","lang":"python3","question_id":2917,"title_slug":"count-pairs-whose-sum-is-less-than-target","code":"class Solution:\n    def countPairs(self, nums: List[int], target: int) -> int:\n        pairs_count = 0\n        nums_count = len(nums)\n        for i in range(nums_count): \n            num1 = nums[i]\n            for j in range(i + 1, nums_count):\n                if num1 + nums[j] < target:\n                    pairs_count += 1\n        \n        return pairs_count","title":"Count Pairs Whose Sum is Less than Target","url":"/submissions/detail/1025770416/","lang_name":"Python3","time":"5 months, 2 weeks","timestamp":1692455810,"status":10,"runtime":"50 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs_count = 0
        nums_count = len(nums)
        for i in range(nums_count):
            num1 = nums[i]
            for j in range(i + 1, nums_count):
                if num1 + nums[j] < target:
                    pairs_count += 1

        return pairs_count
