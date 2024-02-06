// Submission title: for Binary Tree Zigzag Level Order Traversal
// Submission url  : https://leetcode.com/submissions/detail/1087501208/
// Submission json : {"id": 1087501208, "status_display": "Accepted", "lang": "golang", "question_id": 103, "title_slug": "binary-tree-zigzag-level-order-traversal", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc zigzagLevelOrder(root *TreeNode) [][]int {\n    if root == nil {\n        return [][]int{}\n    }\n\n    queue, answer := []*TreeNode{root}, [][]int{}\n    ltr := true\n\n    for length := len(queue); length != 0; length = len(queue) {\n        answerRow := []int{}\n        for i := 0; i < length; i++ {\n            node := queue[i]\n            if node.Left != nil {\n                queue = append(queue, node.Left)\n            }\n            if node.Right != nil {\n                queue = append(queue, node.Right)\n            }\n            answerRow = append(answerRow, node.Val)\n        }\n        if !ltr {\n            slices.Reverse(answerRow)\n        }\n        queue = queue[length:]\n        ltr = !ltr\n        answer = append(answer, answerRow)\n    }\n\n    return answer\n}", "title": "Binary Tree Zigzag Level Order Traversal", "url": "/submissions/detail/1087501208/", "lang_name": "Go", "time": "3\u00a0months, 1\u00a0week", "timestamp": 1698665566, "status": 10, "runtime": "2 ms", "is_pending": "Not Pending", "memory": "2.6 MB", "compare_result": "111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	if root == nil {
		return [][]int{}
	}

	queue, answer := []*TreeNode{root}, [][]int{}
	ltr := true

	for length := len(queue); length != 0; length = len(queue) {
		answerRow := []int{}
		for i := 0; i < length; i++ {
			node := queue[i]
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
			answerRow = append(answerRow, node.Val)
		}
		if !ltr {
			slices.Reverse(answerRow)
		}
		queue = queue[length:]
		ltr = !ltr
		answer = append(answer, answerRow)
	}

	return answer
}
