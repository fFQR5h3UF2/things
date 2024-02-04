# Submission for Trapping Rain Water
# Submission url: https://leetcode.com/submissions/detail/1037777045/


class Solution:
    def trap(self, height: List[int]) -> int:
        left_edge, left_edge_val = -1, -1
        volume, cur_volume = 0, 0
        heights_count = len(height)

        i = 0
        while i < heights_count:
            cur_height = height[i]

            if cur_height < left_edge_val:
                cur_volume += left_edge_val - cur_height
            else:
                left_edge, left_edge_val = i, cur_height
                volume += cur_volume
                cur_volume = 0

            i += 1

            if i == heights_count and cur_volume != 0:
                left_edge, left_edge_val = left_edge + 1, height[left_edge + 1]
                i = left_edge + 1
                cur_volume = 0

        return volume
