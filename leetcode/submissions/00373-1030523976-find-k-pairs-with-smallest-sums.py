# Submission title: Find K Pairs with Smallest Sums
# Submission url  : https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
# Submission url  : https://leetcode.com/submissions/detail/1030523976/"


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
