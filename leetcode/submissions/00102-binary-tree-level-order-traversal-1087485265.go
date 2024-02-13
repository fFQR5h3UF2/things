// Submission title: Binary Tree Level Order Traversal
// Submission url  : https://leetcode.com/problems/binary-tree-level-order-traversal/description/
// Submission url  : https://leetcode.com/submissions/detail/1087485265/
// Submission json : {"id":1087485265,"status_display":"Accepted","lang":"golang","question_id":102,"title_slug":"binary-tree-level-order-traversal","code":"/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc levelOrder(root *TreeNode) [][]int {\n    queue, answer := []*TreeNode{root}, [][]int{}\n\n    for length := len(queue); length != 0; length = len(queue) {\n        answerRow := []int{}\n        for i := 0; i < length; i++ {\n            node := queue[0]\n            queue = queue[1:]\n            if node == nil {\n                continue\n            }\n            answerRow = append(answerRow, node.Val)\n            queue = append(queue, node.Left, node.Right)\n        }\n        if len(answerRow) != 0 {\n            answer = append(answer, answerRow)\n        }\n    }\n\n    return answer\n}","title":"Binary Tree Level Order Traversal","url":"/submissions/detail/1087485265/","lang_name":"Go","time":"3 months, 1 week","timestamp":1698663563,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"3.6 MB","compare_result":"11111111111111111111111111111111111","has_notes":false,"flag_type":1}
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
			queue = queue[1:]
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
