// Submission title: Validate Binary Search Tree
// Submission url  : https://leetcode.com/problems/validate-binary-search-tree/description/"
// Submission url  : https://leetcode.com/submissions/detail/1088457217/"
package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
	if root == nil {
		return false
	}
	return dfs(root.Left, &root.Val, nil) && dfs(root.Right, nil, &root.Val)
}

func dfs(root *TreeNode, max *int, min *int) bool {
	if root == nil {
		return true
	}
	if (max != nil && root.Val >= *max) || (min != nil && root.Val <= *min) {
		return false
	}
	return dfs(root.Left, &root.Val, min) && dfs(root.Right, max, &root.Val)
}
