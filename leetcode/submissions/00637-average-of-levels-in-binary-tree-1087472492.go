// Submission title: for Average of Levels in Binary Tree
// Submission url  : https://leetcode.com/submissions/detail/1087472492/
// Submission json : {"id": 1087472492, "status_display": "Accepted", "lang": "golang", "question_id": 637, "title_slug": "average-of-levels-in-binary-tree", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc averageOfLevels(root *TreeNode) []float64 {\n    if root == nil {\n        return []float64{}\n    }\n    queue, answer := []*TreeNode{root}, []float64{}\n\n    for length := len(queue); length != 0; length = len(queue) {\n        av := 0\n        for i := 0; i < length; i++ {\n            node := queue[0]\n            queue = queue[1:]\n            av += node.Val\n            if left := node.Left; left != nil {\n                queue = append(queue, left)\n            }\n            if right := node.Right; right != nil {\n                queue = append(queue, right)\n            }\n        }\n        answer = append(answer, float64(av) / float64(length))\n    }\n\n    return answer\n}", "title": "Average of Levels in Binary Tree", "url": "/submissions/detail/1087472492/", "lang_name": "Go", "time": "3\u00a0months, 1\u00a0week", "timestamp": 1698661998, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "6.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

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
	queue, answer := []*TreeNode{root}, []float64{}

	for length := len(queue); length != 0; length = len(queue) {
		av := 0
		for i := 0; i < length; i++ {
			node := queue[0]
			queue = queue[1:]
			av += node.Val
			if left := node.Left; left != nil {
				queue = append(queue, left)
			}
			if right := node.Right; right != nil {
				queue = append(queue, right)
			}
		}
		answer = append(answer, float64(av)/float64(length))
	}

	return answer
}
