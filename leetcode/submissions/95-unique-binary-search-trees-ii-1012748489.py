# Submission for Unique Binary Search Trees II
# Submission url: https://leetcode.com/submissions/detail/1012748489/


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def generate_trees(left, rright) -> Generator[None, None, Optional[TreeNode]]:
            if left > right:
                yield None
                return

            for val in range(left, right + 1):
                for left in generate_trees(left, val - 1):
                    for right in generate_trees(val + 1, rright):
                        yield TreeNode(val, left, right)

        return tuple(generate_trees(1, n))
