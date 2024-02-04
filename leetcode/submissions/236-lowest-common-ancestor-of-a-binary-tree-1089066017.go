// Submission for Lowest Common Ancestor of a Binary Tree
// Submission url: https://leetcode.com/submissions/detail/1089066017/

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    isAncestorMap := map[int][2]bool{}
    dfs(root, p, q, isAncestorMap)

    for {
        left, right := root.Left, root.Right
        if left != nil {
            isAncestor := isAncestorMap[left.Val]
            if isAncestor[0] && isAncestor[1] {
                root = left
                continue
            }
        }
        if right != nil {
            isAncestor := isAncestorMap[right.Val]
            if isAncestor[0] && isAncestor[1] {
                root = right
                continue
            }
        }
        break
    }
    return root
}

func dfs(root, p, q *TreeNode, isAncestorMap map[int][2]bool) (bool, bool)  {
    if root == p {
        return true, false
    }
    if root == q {
        return false, true
    }
    hasLeft, _ := dfs(root.Left, p, q, isAncestorMap)
    _, hasRight := dfs(root.Right, p, q, isAncestorMap)
    isAncestorMap[root.Val] = [2]bool{hasLeft, hasRight}
    return hasLeft, hasRight
}
