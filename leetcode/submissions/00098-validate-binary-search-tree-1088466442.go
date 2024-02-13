// Submission title: Validate Binary Search Tree
// Submission url  : https://leetcode.com/problems/validate-binary-search-tree/description/
// Submission url  : https://leetcode.com/submissions/detail/1088466442/
// Submission json : {"id":1088466442,"status_display":"Accepted","lang":"golang","question_id":98,"title_slug":"validate-binary-search-tree","code":"/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\ntype queueItem struct  {\n    node *TreeNode\n    max *int\n    min *int\n}\n\nfunc isValidBST(root *TreeNode) bool {\n    queue := []queueItem{queueItem{root, nil, nil}}\n    for length := len(queue); length > 0; length = len(queue) {\n        for i := 0; i < length; i++ {\n            item := queue[i]\n            if item.node == nil {\n                continue\n            }\n            node := item.node\n            if (item.max != nil && node.Val >= *item.max) || (item.min != nil && node.Val <= *item.min) {\n                return false\n            }\n            queue = append(\n                queue, \n                queueItem{node.Left, &node.Val, item.min}, \n                queueItem{node.Right, item.max, &node.Val},\n            )\n        }\n        queue = queue[length:]\n    }\n    return true\n}","title":"Validate Binary Search Tree","url":"/submissions/detail/1088466442/","lang_name":"Go","time":"3 months","timestamp":1698768725,"status":10,"runtime":"9 ms","is_pending":"Not Pending","memory":"6.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
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
	max  *int
	min  *int
}

func isValidBST(root *TreeNode) bool {
	queue := []queueItem{queueItem{root, nil, nil}}
	for length := len(queue); length > 0; length = len(queue) {
		for i := 0; i < length; i++ {
			item := queue[i]
			if item.node == nil {
				continue
			}
			node := item.node
			if (item.max != nil && node.Val >= *item.max) || (item.min != nil && node.Val <= *item.min) {
				return false
			}
			queue = append(
				queue,
				queueItem{node.Left, &node.Val, item.min},
				queueItem{node.Right, item.max, &node.Val},
			)
		}
		queue = queue[length:]
	}
	return true
}
