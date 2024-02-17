// Submission title: Two Sum IV - Input is a BST
// Submission url  : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/"
// Submission url  : https://leetcode.com/submissions/detail/690025524/"
package submissions

func construct(root *TreeNode, results map[int]int) {
	if root == nil {
		return
	}
	if results[root.Val] < 2 {
		results[root.Val] += 1
	}
	construct(root.Left, results)
	construct(root.Right, results)
}

func findTarget(root *TreeNode, target int) bool {
	results := map[int]int{}
	construct(root, results)
	for number, count := range results {
		if count == 2 && number*2 == target {
			return true
		}
		for number_inner := range results {
			if number_inner <= number {
				continue
			}
			if number+number_inner == target {
				return true
			}
		}
	}
	return false
}
