// Submission for Validate Binary Search Tree
// Submission url: https://leetcode.com/submissions/detail/1088435295/

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
            if left != nil && left.Val >= val {
                return false
            } else if left != nil {
                queue = append(queue, left)
            }
            if right != nil && right.Val <= val {
                return false
            } else if right != nil {
                queue = append(queue, right)
            }
        }
        queue = queue[length:]
    }
    return true
}
