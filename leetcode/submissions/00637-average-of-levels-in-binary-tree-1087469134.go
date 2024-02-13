// Submission title: Average of Levels in Binary Tree
// Submission url  : https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
// Submission url  : https://leetcode.com/submissions/detail/1087469134/
// Submission json : {"id":1087469134,"status_display":"Accepted","lang":"golang","question_id":637,"title_slug":"average-of-levels-in-binary-tree","code":"/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc averageOfLevels(root *TreeNode) []float64 {\n    if root == nil {\n        return []float64{}\n    }\n    qCur, qNext, answer := []*TreeNode{root}, []*TreeNode{}, []float64{}\n\n    for len(qCur) != 0 {\n        av := 0\n        for _, node := range qCur {\n            av += node.Val\n            if left := node.Left; left != nil {\n                qNext = append(qNext, left)\n            }\n            if right := node.Right; right != nil {\n                qNext = append(qNext, right)\n            }\n        }\n        answer = append(answer, float64(av) / float64(len(qCur)))\n        qCur = qCur[:0]\n        qCur, qNext = qNext, qCur\n    }\n\n    return answer\n}","title":"Average of Levels in Binary Tree","url":"/submissions/detail/1087469134/","lang_name":"Go","time":"3 months, 1 week","timestamp":1698661597,"status":10,"runtime":"4 ms","is_pending":"Not Pending","memory":"6.6 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfLevels(root *TreeNode) []float64 {
	if root == nil {
		return []float64{}
	}
	qCur, qNext, answer := []*TreeNode{root}, []*TreeNode{}, []float64{}

	for len(qCur) != 0 {
		av := 0
		for _, node := range qCur {
			av += node.Val
			if left := node.Left; left != nil {
				qNext = append(qNext, left)
			}
			if right := node.Right; right != nil {
				qNext = append(qNext, right)
			}
		}
		answer = append(answer, float64(av)/float64(len(qCur)))
		qCur = qCur[:0]
		qCur, qNext = qNext, qCur
	}

	return answer
}
