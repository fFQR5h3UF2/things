// Submission for Two Sum IV - Input is a BST
// Submission url: https://leetcode.com/submissions/detail/690016895/

package submissions


var results map[int]bool

func findTarget(root *TreeNode, target int) bool {
	if results == nil {
		results = make(map[int]bool)
	}
    if root == nil {
		return false
	}
	for number := range results {
		if root.Val+number == target {
			return true
		}
	}
	results[root.Val] = true
	result_left := findTarget(root.Left, target)
	result_right := findTarget(root.Right, target)
	return result_left || result_right
}
