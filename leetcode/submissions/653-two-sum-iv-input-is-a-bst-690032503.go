// Submission for Two Sum IV - Input is a BST
// Submission url: https://leetcode.com/submissions/detail/690032503/

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
	if len(results) == 0 {
		return false
	}
	for index := 0; index < 10; index++ {
		count, exists := results[index]
		if !exists {
			results[index] = 0
			continue
		}
		if count == 2 && index*2 == target {
			return true
		}
	}
	for index := 0; index < 10; index++ {
		if results[index] == 0 {
			continue
		}
		for index_inner := index + 1; index_inner < 10; index_inner++ {
			if results[index_inner] == 0 {
				continue
			}
			if index+index_inner == target {
				return true
			}
		}
	}
	return false
}
