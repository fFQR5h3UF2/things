// Submission title: for Sum Root to Leaf Numbers
// Submission url  : https://leetcode.com/submissions/detail/1089101627/
// Submission json : {"id": 1089101627, "status_display": "Accepted", "lang": "golang", "question_id": 129, "title_slug": "sum-root-to-leaf-numbers", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc sumNumbers(root *TreeNode) int {\n    return getSum(root, 0)\n}\n\nfunc getSum(root *TreeNode, parentVal int) int {\n    if root == nil {\n        return 0\n    }\n    newVal := root.Val + parentVal * 10\n    if root.Left == nil && root.Right == nil {\n        return newVal\n    }\n    return getSum(root.Left, newVal) + getSum(root.Right, newVal)\n}", "title": "Sum Root to Leaf Numbers", "url": "/submissions/detail/1089101627/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698843078, "status": 10, "runtime": "2 ms", "is_pending": "Not Pending", "memory": "2.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func sumNumbers(root *TreeNode) int {
	return getSum(root, 0)
}

func getSum(root *TreeNode, parentVal int) int {
	if root == nil {
		return 0
	}
	newVal := root.Val + parentVal*10
	if root.Left == nil && root.Right == nil {
		return newVal
	}
	return getSum(root.Left, newVal) + getSum(root.Right, newVal)
}
