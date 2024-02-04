// Submission for Two Sum IV - Input is a BST
// Submission url: https://leetcode.com/submissions/detail/690008861/

package submissions

func findTarget(root *TreeNode, target int) (result bool) {
	current := []*TreeNode{root}
	for {
		var new_current []*TreeNode
		for index, node := range current {
			if node == nil {
				continue
			}
			if node.Left != nil {
				new_current = append(new_current, node.Left)
			}
			if node.Right != nil {
				new_current = append(new_current, node.Right)
			}
			for index_inner := index + 1; index_inner < len(current); index_inner++ {
				current_node := current[index_inner]
				if current_node == nil {
					continue
				}
				if current_node.Val+node.Val == target {
					return true
				}
			}
		}
		current = new_current
		if len(current) == 0 {
			return
		}
	}
}
