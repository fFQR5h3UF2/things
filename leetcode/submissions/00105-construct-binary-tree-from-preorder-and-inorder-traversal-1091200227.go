// Submission title: for Construct Binary Tree from Preorder and Inorder Traversal
// Submission url  : https://leetcode.com/submissions/detail/1091200227/
// Submission json : {"id": 1091200227, "status_display": "Accepted", "lang": "golang", "question_id": 105, "title_slug": "construct-binary-tree-from-preorder-and-inorder-traversal", "code": "func buildTree(preorder []int, inorder []int) *TreeNode {\n\tn := len(inorder)\n\n\tif n == 0 {\n\t\treturn nil\n\t}\n\n\tpv := preorder[0]\n\tpi := 0\n\tfor pi < n && inorder[pi] != pv {\n\t\tpi++\n\t}\n\n\tans := new(TreeNode)\n\tans.Val = pv\n\tans.Left = buildTree(preorder[1:], inorder[:pi])\n\tans.Right = buildTree(preorder[1+pi:], inorder[pi+1:])\n\n\treturn ans\n}\n", "title": "Construct Binary Tree from Preorder and Inorder Traversal", "url": "/submissions/detail/1091200227/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093631, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func buildTree(preorder []int, inorder []int) *TreeNode {
	n := len(inorder)

	if n == 0 {
		return nil
	}

	pv := preorder[0]
	pi := 0
	for pi < n && inorder[pi] != pv {
		pi++
	}

	ans := new(TreeNode)
	ans.Val = pv
	ans.Left = buildTree(preorder[1:], inorder[:pi])
	ans.Right = buildTree(preorder[1+pi:], inorder[pi+1:])

	return ans
}
