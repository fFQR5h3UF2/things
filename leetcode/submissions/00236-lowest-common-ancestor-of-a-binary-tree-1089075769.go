// Submission title: Lowest Common Ancestor of a Binary Tree
// Submission url  : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
// Submission url  : https://leetcode.com/submissions/detail/1089075769/
// Submission json : {"id":1089075769,"status_display":"Accepted","lang":"golang","question_id":236,"title_slug":"lowest-common-ancestor-of-a-binary-tree","code":"/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\n\nfunc lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {\n    isAncestorMap := map[int][2]bool{}\n    dfs(root, p, q, isAncestorMap)\n    isAncestor := func (node *TreeNode) bool {\n        if node == nil {\n            return false\n        }\n        hasNodes := isAncestorMap[node.Val]\n        return hasNodes[0] && hasNodes[1]\n    }\n\n    for {\n        left, right := root.Left, root.Right\n        if isAncestor(left) {\n            root = left\n        } else if isAncestor(right) {\n            root = right\n        } else {\n            break\n        }\n    }\n    return root\n}\n\nfunc dfs(root, p, q *TreeNode, isAncestorMap map[int][2]bool) (bool, bool)  {\n    if root == nil {\n        return false, false\n    }\n    hasPLeft, hasQLeft := dfs(root.Left, p, q, isAncestorMap)\n    hasPRight, hasQRight := dfs(root.Right, p, q, isAncestorMap)\n    hasP, hasQ := hasPLeft || hasPRight, hasQLeft || hasQRight\n    if root == p {\n        hasP = true\n    }\n    if root == q {\n        hasQ = true\n    }\n    isAncestorMap[root.Val] = [2]bool{hasP, hasQ}\n    return hasP, hasQ\n}","title":"Lowest Common Ancestor of a Binary Tree","url":"/submissions/detail/1089075769/","lang_name":"Go","time":"3 months","timestamp":1698840005,"status":10,"runtime":"15 ms","is_pending":"Not Pending","memory":"8.1 MB","compare_result":"1111111111111111111111111111111","has_notes":false,"flag_type":1}
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
	isAncestorMap := map[int][2]bool{}
	dfs(root, p, q, isAncestorMap)
	isAncestor := func(node *TreeNode) bool {
		if node == nil {
			return false
		}
		hasNodes := isAncestorMap[node.Val]
		return hasNodes[0] && hasNodes[1]
	}

	for {
		left, right := root.Left, root.Right
		if isAncestor(left) {
			root = left
		} else if isAncestor(right) {
			root = right
		} else {
			break
		}
	}
	return root
}

func dfs(root, p, q *TreeNode, isAncestorMap map[int][2]bool) (bool, bool) {
	if root == nil {
		return false, false
	}
	hasPLeft, hasQLeft := dfs(root.Left, p, q, isAncestorMap)
	hasPRight, hasQRight := dfs(root.Right, p, q, isAncestorMap)
	hasP, hasQ := hasPLeft || hasPRight, hasQLeft || hasQRight
	if root == p {
		hasP = true
	}
	if root == q {
		hasQ = true
	}
	isAncestorMap[root.Val] = [2]bool{hasP, hasQ}
	return hasP, hasQ
}
