// Submission title: for Flatten Binary Tree to Linked List
// Submission url  : https://leetcode.com/submissions/detail/1090504012/
// Submission json : {"id": 1090504012, "status_display": "Accepted", "lang": "golang", "question_id": 114, "title_slug": "flatten-binary-tree-to-linked-list", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc flatten(root *TreeNode)  {\n    if root == nil {\n        return\n    }\n    right := root.Right\n    root.Right = nil\n    list := &TreeNode{0, nil, nil}\n    listTail := flattenNode(root, list)\n    if right != nil {\n        flattenNode(right, listTail)\n    }\n}\n\nfunc flattenNode(node, listTail *TreeNode) *TreeNode {\n    left, right := node.Left, node.Right\n    node.Left, node.Right = nil, nil\n    listTail.Right = node\n    listTail = listTail.Right\n    if left != nil {\n        listTail = flattenNode(left, listTail)\n    }\n    if right != nil {\n        listTail = flattenNode(right, listTail)\n    }\n    return listTail\n}", "title": "Flatten Binary Tree to Linked List", "url": "/submissions/detail/1090504012/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699004405, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "2.9 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func flatten(root *TreeNode) {
	if root == nil {
		return
	}
	right := root.Right
	root.Right = nil
	list := &TreeNode{0, nil, nil}
	listTail := flattenNode(root, list)
	if right != nil {
		flattenNode(right, listTail)
	}
}

func flattenNode(node, listTail *TreeNode) *TreeNode {
	left, right := node.Left, node.Right
	node.Left, node.Right = nil, nil
	listTail.Right = node
	listTail = listTail.Right
	if left != nil {
		listTail = flattenNode(left, listTail)
	}
	if right != nil {
		listTail = flattenNode(right, listTail)
	}
	return listTail
}
