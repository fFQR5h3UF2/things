// Submission title: for Construct Binary Tree from Inorder and Postorder Traversal
// Submission url  : https://leetcode.com/submissions/detail/1091200359/
// Submission json : {"id": 1091200359, "status_display": "Accepted", "lang": "golang", "question_id": 106, "title_slug": "construct-binary-tree-from-inorder-and-postorder-traversal", "code": "func buildTree(inorder []int, postorder []int) *TreeNode {\n\tn := len(postorder)\n\tif n == 0 {\n\t\treturn nil\n\t}\n\n\tpivotId := 0\n\tfor pivotId < n && inorder[pivotId] != postorder[n-1] {\n\t\tpivotId++\n\t}\n\n\troot := new(TreeNode)\n\troot.Val = postorder[n-1]\n\troot.Left = buildTree(inorder[:pivotId], postorder[:pivotId])\n\troot.Right = buildTree(inorder[pivotId+1:], postorder[pivotId:n-1])\n\treturn root\n}\n", "title": "Construct Binary Tree from Inorder and Postorder Traversal", "url": "/submissions/detail/1091200359/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093649, "status": 10, "runtime": "7 ms", "is_pending": "Not Pending", "memory": "3.7 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func buildTree(inorder []int, postorder []int) *TreeNode {
	n := len(postorder)
	if n == 0 {
		return nil
	}

	pivotId := 0
	for pivotId < n && inorder[pivotId] != postorder[n-1] {
		pivotId++
	}

	root := new(TreeNode)
	root.Val = postorder[n-1]
	root.Left = buildTree(inorder[:pivotId], postorder[:pivotId])
	root.Right = buildTree(inorder[pivotId+1:], postorder[pivotId:n-1])
	return root
}
