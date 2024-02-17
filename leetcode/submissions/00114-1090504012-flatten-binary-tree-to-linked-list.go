// Submission title: Flatten Binary Tree to Linked List
// Submission url  : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/"
// Submission url  : https://leetcode.com/submissions/detail/1090504012/"
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
