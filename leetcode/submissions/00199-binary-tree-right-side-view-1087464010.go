// Submission title: Binary Tree Right Side View
// Submission url  : https://leetcode.com/problems/binary-tree-right-side-view/description/
// Submission url  : https://leetcode.com/submissions/detail/1087464010/
// Submission json : {"id":1087464010,"status_display":"Accepted","lang":"golang","question_id":199,"title_slug":"binary-tree-right-side-view","code":"/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc rightSideView(root *TreeNode) []int {\n    if root == nil {\n        return []int{}\n    }\n\n    q_cur, q_next, answer := []*TreeNode{root}, []*TreeNode{}, []int{}\n\n    for len(q_cur) != 0 {\n        for _, node := range q_cur {\n            if left := node.Left; left != nil {\n                q_next = append(q_next, left)\n            }\n            if right := node.Right; right != nil {\n                q_next = append(q_next, right)\n            }\n        }\n\n        answer = append(answer, q_cur[len(q_cur) - 1].Val)\n        q_cur = q_cur[:0]\n        q_cur, q_next = q_next, q_cur\n    }\n\n    return answer\n} ","title":"Binary Tree Right Side View","url":"/submissions/detail/1087464010/","lang_name":"Go","time":"3 months, 1 week","timestamp":1698661028,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"2.2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
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

	q_cur, q_next, answer := []*TreeNode{root}, []*TreeNode{}, []int{}

	for len(q_cur) != 0 {
		for _, node := range q_cur {
			if left := node.Left; left != nil {
				q_next = append(q_next, left)
			}
			if right := node.Right; right != nil {
				q_next = append(q_next, right)
			}
		}

		answer = append(answer, q_cur[len(q_cur)-1].Val)
		q_cur = q_cur[:0]
		q_cur, q_next = q_next, q_cur
	}

	return answer
}
