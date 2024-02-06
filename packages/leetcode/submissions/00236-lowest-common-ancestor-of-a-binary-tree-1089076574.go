// Submission title: for Lowest Common Ancestor of a Binary Tree
// Submission url  : https://leetcode.com/submissions/detail/1089076574/
// Submission json : {"id": 1089076574, "status_display": "Accepted", "lang": "golang", "question_id": 236, "title_slug": "lowest-common-ancestor-of-a-binary-tree", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\n func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {\n    if root == nil {\n\t\treturn nil\n\t}\n    if root == p || root == q {\n\t\treturn root\n\t}\n    left, right := lowestCommonAncestor(root.Left, p, q), lowestCommonAncestor(root.Right, p, q)\n    if left != nil && right != nil {\n\t\treturn root\n\t}\n\tif left != nil {\n\t\treturn left\n\t}\n\treturn right\n}", "title": "Lowest Common Ancestor of a Binary Tree", "url": "/submissions/detail/1089076574/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698840113, "status": 10, "runtime": "6 ms", "is_pending": "Not Pending", "memory": "7 MB", "compare_result": "1111111111111111111111111111111", "has_notes": true, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil {
		return nil
	}
	if root == p || root == q {
		return root
	}
	left, right := lowestCommonAncestor(root.Left, p, q), lowestCommonAncestor(root.Right, p, q)
	if left != nil && right != nil {
		return root
	}
	if left != nil {
		return left
	}
	return right
}
