# Submission for Minimum Operations to Reduce X to Zero
# Submission url: https://leetcode.com/submissions/detail/1054331408/


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        length = len(nums)
        queue = [(0, length - 1, x)]
        results_heap = []
        while queue:
            left, right, val = queue.pop()
            if val == 0:
                heappush(results_heap, left + length - 1 - right)
            elif left == right and nums[left] == val:
                heappush(results_heap, length)
            elif left != right and val > 0:
                queue.append((left + 1, right, val - nums[left]))
                queue.append((left, right - 1, val - nums[right]))

        return results_heap[0] if results_heap else -1
