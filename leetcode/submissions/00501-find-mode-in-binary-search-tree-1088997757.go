// Submission for Find Mode in Binary Search Tree
// Submission url: https://leetcode.com/submissions/detail/1088997757/

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findMode(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	counter := map[int]int{}
	queue := []*TreeNode{root}
	for length := len(queue); length > 0; length = len(queue) {
		for i := 0; i < length; i++ {
			node := queue[i]
			if _, ok := counter[node.Val]; ok {
				counter[node.Val] += 1
			} else {
				counter[node.Val] = 1
			}
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		queue = queue[length:]
	}
	maxCount, answer := 0, []int{}
	for key, count := range counter {
		if count < maxCount {
			continue
		}
		if count > maxCount {
			answer = answer[:0]
			maxCount = count
		}
		answer = append(answer, key)
	}
	return answer
}
