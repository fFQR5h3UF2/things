// Submission for Validate Binary Search Tree
// Submission url: https://leetcode.com/submissions/detail/1088451991/

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
    if root == nil {
        return false
    }
    return dfs(root.Left, root.Val, math.MinInt32) && dfs(root.Right, math.MaxInt32, root.Val)
}

func dfs(root *TreeNode, max int, min int) bool {
    if root == nil {
        return true
    }
    if root.Val >= max || root.Val <= min {
        return false
    }
    return dfs(root.Left, root.Val, min) && dfs(root.Right, max, root.Val)

}
