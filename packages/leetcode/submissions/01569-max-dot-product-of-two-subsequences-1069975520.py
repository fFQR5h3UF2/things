# Submission title: for Max Dot Product of Two Subsequences
# Submission url  : https://leetcode.com/submissions/detail/1069975520/
# Submission json : {"id": 1069975520, "status_display": "Accepted", "lang": "python3", "question_id": 1569, "title_slug": "max-dot-product-of-two-subsequences", "code": "class Solution:\n    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:\n        @cache\n        def dp(i, j):\n            if i == len(nums1) or j == len(nums2):\n                return 0\n            \n            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)\n            return max(use, dp(i + 1, j), dp(i, j + 1))\n            \n        if max(nums1) < 0 and min(nums2) > 0:\n            return max(nums1) * min(nums2)\n        \n        if min(nums1) > 0 and max(nums2) < 0:\n            return min(nums1) * max(nums2)\n        \n        return dp(0, 0)", "title": "Max Dot Product of Two Subsequences", "url": "/submissions/detail/1069975520/", "lang_name": "Python3", "time": "3\u00a0months, 4\u00a0weeks", "timestamp": 1696750784, "status": 10, "runtime": "482 ms", "is_pending": "Not Pending", "memory": "98.9 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(i, j):
            if i == len(nums1) or j == len(nums2):
                return 0

            use = nums1[i] * nums2[j] + dp(i + 1, j + 1)
            return max(use, dp(i + 1, j), dp(i, j + 1))

        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)

        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)

        return dp(0, 0)
