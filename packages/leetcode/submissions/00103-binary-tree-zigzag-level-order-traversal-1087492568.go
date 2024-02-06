// Submission title: for Binary Tree Zigzag Level Order Traversal
// Submission url  : https://leetcode.com/submissions/detail/1087492568/
// Submission json : {"id": 1087492568, "status_display": "Accepted", "lang": "golang", "question_id": 103, "title_slug": "binary-tree-zigzag-level-order-traversal", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc zigzagLevelOrder(root *TreeNode) [][]int {\n    if root == nil {\n        return [][]int{}\n    }\n\n    queue, answer := []*TreeNode{root}, [][]int{}\n    leftToRight := true\n\n    for length := len(queue); length != 0; length = len(queue) {\n        answerRow := []int{}\n\n        for i := 0; i < length; i++ {\n            node := queue[0]\n            queue = queue[1:]\n\n            answerRow = append(answerRow, node.Val)\n            if left := node.Left; left != nil {\n                queue = append(queue, left)\n            }\n            if right := node.Right; right != nil {\n                queue = append(queue, right)\n            }\n        }\n        if !leftToRight {\n            slices.Reverse(answerRow)\n        }\n        leftToRight = !leftToRight\n        answer = append(answer, answerRow)\n    }\n\n    return answer\n}", "title": "Binary Tree Zigzag Level Order Traversal", "url": "/submissions/detail/1087492568/", "lang_name": "Go", "time": "3\u00a0months, 1\u00a0week", "timestamp": 1698664487, "status": 10, "runtime": "1 ms", "is_pending": "Not Pending", "memory": "2.5 MB", "compare_result": "111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

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
	leftToRight := true

	for length := len(queue); length != 0; length = len(queue) {
		answerRow := []int{}

		for i := 0; i < length; i++ {
			node := queue[0]
			queue = queue[1:]

			answerRow = append(answerRow, node.Val)
			if left := node.Left; left != nil {
				queue = append(queue, left)
			}
			if right := node.Right; right != nil {
				queue = append(queue, right)
			}
		}
		if !leftToRight {
			slices.Reverse(answerRow)
		}
		leftToRight = !leftToRight
		answer = append(answer, answerRow)
	}

	return answer
}
