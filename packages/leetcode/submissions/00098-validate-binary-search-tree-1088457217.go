// Submission title: for Validate Binary Search Tree
// Submission url  : https://leetcode.com/submissions/detail/1088457217/
// Submission json : {"id": 1088457217, "status_display": "Accepted", "lang": "golang", "question_id": 98, "title_slug": "validate-binary-search-tree", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc isValidBST(root *TreeNode) bool {\n    if root == nil {\n        return false\n    }\n    return dfs(root.Left, &root.Val, nil) && dfs(root.Right, nil, &root.Val)\n}\n\nfunc dfs(root *TreeNode, max *int, min *int) bool {\n    if root == nil {\n        return true\n    }\n    if (max != nil && root.Val >= *max) || (min != nil && root.Val <= *min) {\n        return false\n    }\n    return dfs(root.Left, &root.Val, min) && dfs(root.Right, max, &root.Val)\n}", "title": "Validate Binary Search Tree", "url": "/submissions/detail/1088457217/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698767957, "status": 10, "runtime": "6 ms", "is_pending": "Not Pending", "memory": "5.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}

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
