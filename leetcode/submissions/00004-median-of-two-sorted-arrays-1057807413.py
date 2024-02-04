# Submission title: for Median of Two Sorted Arrays
# Submission url  : https://leetcode.com/submissions/detail/1057807413/
# Submission json : {"id": 1057807413, "status_display": "Accepted", "lang": "python3", "question_id": 4, "title_slug": "median-of-two-sorted-arrays", "code": "class Solution:\n    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:\n        m, n = len(nums1), len(nums2)\n        p1, p2 = 0, 0\n        \n        # Get the smaller value between nums1[p1] and nums2[p2].\n        def get_min():\n            nonlocal p1, p2\n            if p1 < m and p2 < n:\n                if nums1[p1] < nums2[p2]:\n                    ans = nums1[p1]\n                    p1 += 1\n                else:\n                    ans = nums2[p2]\n                    p2 += 1\n            elif p2 == n:\n                ans = nums1[p1]\n                p1 += 1\n            else:\n                ans = nums2[p2]\n                p2 += 1\n            return ans\n        \n        if (m + n) % 2 == 0:\n            for _ in range((m + n) // 2 - 1):\n                _ = get_min()\n            return (get_min() + get_min()) / 2\n        else:\n            for _ in range((m + n) // 2):\n                _ = get_min()\n            return get_min()", "title": "Median of Two Sorted Arrays", "url": "/submissions/detail/1057807413/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695549192, "status": 10, "runtime": "90 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1, p2 = 0, 0

        # Get the smaller value between nums1[p1] and nums2[p2].
        def get_min():
            nonlocal p1, p2
            if p1 < m and p2 < n:
                if nums1[p1] < nums2[p2]:
                    ans = nums1[p1]
                    p1 += 1
                else:
                    ans = nums2[p2]
                    p2 += 1
            elif p2 == n:
                ans = nums1[p1]
                p1 += 1
            else:
                ans = nums2[p2]
                p2 += 1
            return ans

        if (m + n) % 2 == 0:
            for _ in range((m + n) // 2 - 1):
                _ = get_min()
            return (get_min() + get_min()) / 2
        else:
            for _ in range((m + n) // 2):
                _ = get_min()
            return get_min()
