// Submission for Two Sum IV - Input is a BST
// Submission url: https://leetcode.com/submissions/detail/690019034/

package submissions


var results map[int]int

func findTarget(root *TreeNode, target int) bool {
	if results == nil {
		results = make(map[int]int)
	}
	if root == nil {
		return false
	}
    	if results[root.Val] < 3 {
		results[root.Val] += 1
	}
	for number, count := range results {
		if number == root.Val && count < 2 {
			continue
		}
		if root.Val+number == target {
			return true
		}
	}

	result_left := findTarget(root.Left, target)
	result_right := findTarget(root.Right, target)
	return result_left || result_right
}
