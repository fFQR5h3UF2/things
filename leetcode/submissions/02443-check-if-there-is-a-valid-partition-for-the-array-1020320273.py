# Submission title: Check if There is a Valid Partition For The Array
# Submission url  : https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1020320273/
# Submission json : {"id":1020320273,"status_display":"Accepted","lang":"python3","question_id":2443,"title_slug":"check-if-there-is-a-valid-partition-for-the-array","code":"class Solution:\n    def validPartition(self, nums: List[int]) -> bool:\n        n = len(nums)\n        dp = [True] + [False] * n\n\n        # Determine if the prefix array nums[0 ~ i] has a valid partition\n        for i in range(n):\n            dp_index = i + 1\n\n            # Check 3 possibilities\n            if i > 0 and nums[i] == nums[i - 1]:\n                dp[dp_index] |= dp[dp_index - 2]\n            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:\n                dp[dp_index] |= dp[dp_index - 3]\n            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:\n                dp[dp_index] |= dp[dp_index - 3]\n \n        return dp[n]","title":"Check if There is a Valid Partition For The Array","url":"/submissions/detail/1020320273/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1691940913,"status":10,"runtime":"907 ms","is_pending":"Not Pending","memory":"30.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True] + [False] * n

        # Determine if the prefix array nums[0 ~ i] has a valid partition
        for i in range(n):
            dp_index = i + 1

            # Check 3 possibilities
            if i > 0 and nums[i] == nums[i - 1]:
                dp[dp_index] |= dp[dp_index - 2]
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                dp[dp_index] |= dp[dp_index - 3]
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                dp[dp_index] |= dp[dp_index - 3]

        return dp[n]
