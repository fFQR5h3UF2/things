// Submission title: Binary Tree Right Side View
// Submission url  : https://leetcode.com/problems/binary-tree-right-side-view/description/
// Submission url  : https://leetcode.com/submissions/detail/1087475497/
// Submission json : {"id":1087475497,"status_display":"Accepted","lang":"golang","question_id":199,"title_slug":"binary-tree-right-side-view","code":"/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc rightSideView(root *TreeNode) []int {\n    if root == nil {\n        return []int{}\n    }\n\n    queue, answer := []*TreeNode{root}, []int{}\n\n    for length := len(queue); length != 0; length = len(queue) {\n        for i := 0; i < length; i++ {\n            node := queue[0]\n            queue = queue[1:]\n            if i == length - 1 {\n                answer = append(answer, node.Val)\n            }\n            if left := node.Left; left != nil {\n                queue = append(queue, left)\n            }\n            if right := node.Right; right != nil {\n                queue = append(queue, right)\n            }\n        }\n    }\n\n    return answer\n} ","title":"Binary Tree Right Side View","url":"/submissions/detail/1087475497/","lang_name":"Go","time":"3 months, 1 week","timestamp":1698662375,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"2.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rightSideView(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}

	queue, answer := []*TreeNode{root}, []int{}

	for length := len(queue); length != 0; length = len(queue) {
		for i := 0; i < length; i++ {
			node := queue[0]
			queue = queue[1:]
			if i == length-1 {
				answer = append(answer, node.Val)
			}
			if left := node.Left; left != nil {
				queue = append(queue, left)
			}
			if right := node.Right; right != nil {
				queue = append(queue, right)
			}
		}
	}

	return answer
}
