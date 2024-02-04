// Submission title: for Sum Root to Leaf Numbers
// Submission url  : https://leetcode.com/submissions/detail/1089106155/
// Submission json : {"id": 1089106155, "status_display": "Accepted", "lang": "golang", "question_id": 129, "title_slug": "sum-root-to-leaf-numbers", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\n\ntype queueItem struct {\n    node *TreeNode\n    sum int\n}\nfunc sumNumbers(root *TreeNode) int {\n    if root == nil {\n        return 0\n    }\n    queue := []queueItem{queueItem{root, 0}}\n    sum := 0\n    for length := len(queue); length > 0; length = len(queue) {\n        for i := 0; i < length; i++ {\n            item := queue[i]\n            if item.node == nil {\n                continue\n            }\n            left, right, newVal := item.node.Left, item.node.Right, item.node.Val + item.sum * 10\n            if left == nil && right == nil {\n                sum += newVal\n            } else {\n                queue = append(queue, queueItem{left, newVal}, queueItem{right, newVal})\n            }\n        }\n        queue = queue[length:]\n    }\n    return sum\n}", "title": "Sum Root to Leaf Numbers", "url": "/submissions/detail/1089106155/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698843559, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "2.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type queueItem struct {
	node *TreeNode
	sum  int
}

func sumNumbers(root *TreeNode) int {
	if root == nil {
		return 0
	}
	queue := []queueItem{queueItem{root, 0}}
	sum := 0
	for length := len(queue); length > 0; length = len(queue) {
		for i := 0; i < length; i++ {
			item := queue[i]
			if item.node == nil {
				continue
			}
			left, right, newVal := item.node.Left, item.node.Right, item.node.Val+item.sum*10
			if left == nil && right == nil {
				sum += newVal
			} else {
				queue = append(queue, queueItem{left, newVal}, queueItem{right, newVal})
			}
		}
		queue = queue[length:]
	}
	return sum
}
