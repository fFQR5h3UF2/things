// Submission for Construct Binary Tree from Inorder and Postorder Traversal
// Submission url: https://leetcode.com/submissions/detail/1091200359/

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
