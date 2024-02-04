// Submission title: for Binary Tree Level Order Traversal
// Submission url  : https://leetcode.com/submissions/detail/1087481177/
// Submission json : {"id": 1087481177, "status_display": "Accepted", "lang": "golang", "question_id": 102, "title_slug": "binary-tree-level-order-traversal", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc levelOrder(root *TreeNode) [][]int {\n    if root == nil {\n        return [][]int{}\n    }\n\n    stack, answer := []*TreeNode{root}, [][]int{}\n\n    for length := len(stack); length != 0; length = len(stack) {\n        answerRow := []int{}\n        for i := 0; i < length; i++ {\n            node := stack[0]\n            answerRow = append(answerRow, node.Val)\n            stack = stack[1:]\n            if left := node.Left; left != nil {\n                stack = append(stack, node.Left)\n            }\n            if right := node.Right; right != nil {\n                stack = append(stack, node.Right)\n            }\n        }\n        answer = append(answer, answerRow)\n    }\n\n    return answer\n}", "title": "Binary Tree Level Order Traversal", "url": "/submissions/detail/1087481177/", "lang_name": "Go", "time": "3\u00a0months, 1\u00a0week", "timestamp": 1698663075, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "3.6 MB", "compare_result": "11111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

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

	stack, answer := []*TreeNode{root}, [][]int{}

	for length := len(stack); length != 0; length = len(stack) {
		answerRow := []int{}
		for i := 0; i < length; i++ {
			node := stack[0]
			answerRow = append(answerRow, node.Val)
			stack = stack[1:]
			if left := node.Left; left != nil {
				stack = append(stack, node.Left)
			}
			if right := node.Right; right != nil {
				stack = append(stack, node.Right)
			}
		}
		answer = append(answer, answerRow)
	}

	return answer
}
