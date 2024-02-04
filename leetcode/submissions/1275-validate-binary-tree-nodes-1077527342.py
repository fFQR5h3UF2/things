# Submission for Validate Binary Tree Nodes
# Submission url: https://leetcode.com/submissions/detail/1077527342/


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:

        visited = set()

        to_visit = [0]
        while to_visit:
            node = to_visit.pop()
            if node == -1:
                continue
            if node in visited:
                return False
            visited.add(node)
            to_visit.extend((leftChild[node], rightChild[node]))

        return len(visited) == n
