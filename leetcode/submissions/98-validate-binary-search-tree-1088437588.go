// Submission for Validate Binary Search Tree
// Submission url: https://leetcode.com/submissions/detail/1088437588/

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
    queue := []*TreeNode{root}
    for length := len(queue); length > 0; length = len(queue) {
        for i := 0; i < length; i++ {
            node := queue[i]
            left, right, val := node.Left, node.Right, node.Val
            if left == nil && right == nil {
                continue
            }
            if left == nil || right == nil || left.Val >= val || right.Val <= val {
                return false
            }
            queue = append(queue, left, right)
        }
        queue = queue[length:]
    }
    return true
}
