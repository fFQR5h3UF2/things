// Submission title: for Binary Tree Maximum Path Sum
// Submission url  : https://leetcode.com/submissions/detail/1091200483/
// Submission json : {"id": 1091200483, "status_display": "Accepted", "lang": "golang", "question_id": 124, "title_slug": "binary-tree-maximum-path-sum", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc maxPathSum(root *TreeNode) int {\n    ans := -1 << 63\n    maxPath(root, &ans)\n    return ans\n}\n\nfunc maxPath(root *TreeNode, ans *int) int {\n    if root == nil {\n        return 0\n    }\n    leftPathSum := maxPath(root.Left, ans)\n    rightPathSum := maxPath(root.Right, ans)\n    *ans = max(*ans, leftPathSum + rightPathSum + root.Val)\n    return max(max(leftPathSum+root.Val, rightPathSum+root.Val), 0)\n}\n\nfunc max(a int, b int) int {\n    if (a >= b) {\n        return a\n    }\n    return b\n}\n", "title": "Binary Tree Maximum Path Sum", "url": "/submissions/detail/1091200483/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093667, "status": 10, "runtime": "11 ms", "is_pending": "Not Pending", "memory": "8.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxPathSum(root *TreeNode) int {
	ans := -1 << 63
	maxPath(root, &ans)
	return ans
}

func maxPath(root *TreeNode, ans *int) int {
	if root == nil {
		return 0
	}
	leftPathSum := maxPath(root.Left, ans)
	rightPathSum := maxPath(root.Right, ans)
	*ans = max(*ans, leftPathSum+rightPathSum+root.Val)
	return max(max(leftPathSum+root.Val, rightPathSum+root.Val), 0)
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}
