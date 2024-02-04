# Submission for Validate Binary Tree Nodes
# Submission url: https://leetcode.com/submissions/detail/1077617254/


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        reversed_graph = {}

        for i in range(n):
            left, right = leftChild[i], rightChild[i]
            left_valid, right_valid = left != -1, right != -1
            if (left_valid and left in reversed_graph) or (
                right_valid and right in reversed_graph
            ):
                return False
            if left_valid:
                reversed_graph[left] = i
            if right_valid:
                reversed_graph[right] = i
            if i in reversed_graph and reversed_graph[i] in (left, right):
                return False

        return len(reversed_graph) == n - 1
