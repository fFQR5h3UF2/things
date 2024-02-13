# Submission title: Maximum Score of a Good Subarray
# Submission url  : https://leetcode.com/problems/maximum-score-of-a-good-subarray/description/
# Submission url  : https://leetcode.com/submissions/detail/1081281295/
# Submission json : {"id":1081281295,"status_display":"Accepted","lang":"python3","question_id":1918,"title_slug":"maximum-score-of-a-good-subarray","code":"class Solution:\n    def maximumScore(self, nums: List[int], k: int) -> int:\n        n = len(nums)\n        left = k\n        right = k\n        ans = nums[k]\n        curr_min = nums[k]\n        \n        while left > 0 or right < n - 1:\n            if (nums[left - 1] if left else 0) < (nums[right + 1] if right < n - 1 else 0):\n                right += 1\n                curr_min = min(curr_min, nums[right])\n            else:\n                left -= 1\n                curr_min = min(curr_min, nums[left])\n\n            ans = max(ans, curr_min * (right - left + 1))\n        \n        return ans","title":"Maximum Score of a Good Subarray","url":"/submissions/detail/1081281295/","lang_name":"Python3","time":"3 months, 2 weeks","timestamp":1697972267,"status":10,"runtime":"1024 ms","is_pending":"Not Pending","memory":"27.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = k
        right = k
        ans = nums[k]
        curr_min = nums[k]

        while left > 0 or right < n - 1:
            if (nums[left - 1] if left else 0) < (
                nums[right + 1] if right < n - 1 else 0
            ):
                right += 1
                curr_min = min(curr_min, nums[right])
            else:
                left -= 1
                curr_min = min(curr_min, nums[left])

            ans = max(ans, curr_min * (right - left + 1))

        return ans
