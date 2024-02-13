# Submission title: Find K Pairs with Smallest Sums
# Submission url  : https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
# Submission url  : https://leetcode.com/submissions/detail/1030523976/
# Submission json : {"id":1030523976,"status_display":"Accepted","lang":"python3","question_id":373,"title_slug":"find-k-pairs-with-smallest-sums","code":"class Solution:\n    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:\n        nums1_count, nums2_count = len(nums1), len(nums2)\n        result = []\n        visited = set(((0, 0)))\n        min_heap = [(nums1[0] + nums2[0], (0, 0))]\n        count = 0\n\n        while k > 0 and min_heap:\n            _, (i, j) = heappop(min_heap)\n            new_i, new_j = i + 1, j + 1\n            new_pair1, new_pair2 = (new_i, j), (i, new_j)\n            num1, num2 = nums1[i], nums2[j]\n            result.append((num1, num2))\n\n            if new_i < nums1_count and new_pair1 not in visited:\n                heappush(min_heap, (nums1[new_i] + num2, new_pair1))\n                visited.add(new_pair1)\n\n            if new_j < nums2_count and new_pair2 not in visited:\n                heappush(min_heap, (num1 + nums2[new_j], new_pair2))\n                visited.add(new_pair2)\n\n            k -= 1\n        \n        return result","title":"Find K Pairs with Smallest Sums","url":"/submissions/detail/1030523976/","lang_name":"Python3","time":"5 months, 2 weeks","timestamp":1692884526,"status":10,"runtime":"930 ms","is_pending":"Not Pending","memory":"36.5 MB","compare_result":"111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        nums1_count, nums2_count = len(nums1), len(nums2)
        result = []
        visited = set(((0, 0)))
        min_heap = [(nums1[0] + nums2[0], (0, 0))]
        count = 0

        while k > 0 and min_heap:
            _, (i, j) = heappop(min_heap)
            new_i, new_j = i + 1, j + 1
            new_pair1, new_pair2 = (new_i, j), (i, new_j)
            num1, num2 = nums1[i], nums2[j]
            result.append((num1, num2))

            if new_i < nums1_count and new_pair1 not in visited:
                heappush(min_heap, (nums1[new_i] + num2, new_pair1))
                visited.add(new_pair1)

            if new_j < nums2_count and new_pair2 not in visited:
                heappush(min_heap, (num1 + nums2[new_j], new_pair2))
                visited.add(new_pair2)

            k -= 1

        return result
