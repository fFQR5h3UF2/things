// Submission for Binary Tree Level Order Traversal
// Submission url: https://leetcode.com/submissions/detail/1087479319/

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    if root == nil {
        return [][]int{}
    }

    stack, answer := []*TreeNode{}, [][]int{}

    for length := len(stack); length != 0; length = len(stack) {
        for i := 0; i < length; i++ {
            node, answerRow := stack[0], []int{}
            stack = stack[1:]
            if left := node.Left; left != nil {
                stack = append(stack, node.Left)
                answerRow = append(answerRow, left.Val)
            }
            if right := node.Right; right != nil {
                stack = append(stack, node.Right)
                answerRow = append(answerRow, right.Val)
            }
            answer = append(answer, answerRow)
        }
    }

    return answer
}
