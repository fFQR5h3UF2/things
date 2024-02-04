// Submission for Binary Tree Level Order Traversal
// Submission url: https://leetcode.com/submissions/detail/1087485195/

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
    queue, answer := []*TreeNode{root}, [][]int{}

    for length := len(queue); length != 0; length = len(queue) {
        answerRow := []int{}
        for i := 0; i < length; i++ {
            node := queue[0]
            stack = queue[1:]
            if node == nil {
                continue
            }
            answerRow = append(answerRow, node.Val)
            queue = append(queue, node.Left, node.Right)
        }
        if len(answerRow) != 0 {
            answer = append(answer, answerRow)
        }
    }

    return answer
}
