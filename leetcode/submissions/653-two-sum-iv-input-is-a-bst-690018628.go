// Submission for Two Sum IV - Input is a BST
// Submission url: https://leetcode.com/submissions/detail/690018628/

package submissions


var results map[int]int

func findTarget(root *TreeNode, target int) bool {
	if results == nil {
		results = make(map[int]int)
	}
	if root == nil {
		return false
	}
	for number, count := range results {
		if number == root.Val && count < 2 {
			continue
		}
		if root.Val+number == target {
			return true
		}
	}
	if results[root.Val] < 2 {
		results[root.Val] += 1
	}
	result_left := findTarget(root.Left, target)
	result_right := findTarget(root.Right, target)
	return result_left || result_right
}
