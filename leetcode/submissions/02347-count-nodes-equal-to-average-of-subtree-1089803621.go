// Submission title: Count Nodes Equal to Average of Subtree
// Submission url  : https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
// Submission url  : https://leetcode.com/submissions/detail/1089803621/
// Submission json : {"id":1089803621,"status_display":"Accepted","lang":"golang","question_id":2347,"title_slug":"count-nodes-equal-to-average-of-subtree","code":"/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc averageOfSubtree(root *TreeNode) int {\n    _, _, answer := getAverage(root)\n    return answer\n}\n\nfunc getAverage(root *TreeNode) (int, int, int) {\n    if root == nil {\n        return 0, 0, 0\n    }\n    sum, count, validNodes := root.Val, 1, 0\n    leftSum, leftCount, leftValidNodes := getAverage(root.Left)\n    rightSum, rightCount, rightValidNodes := getAverage(root.Right)\n    validNodes += leftValidNodes + rightValidNodes\n    sum += leftSum + rightSum\n    count += leftCount + rightCount\n    if sum / count == root.Val {\n        validNodes += 1\n    }\n    return sum, count, validNodes\n}","title":"Count Nodes Equal to Average of Subtree","url":"/submissions/detail/1089803621/","lang_name":"Go","time":"3 months","timestamp":1698921165,"status":10,"runtime":"5 ms","is_pending":"Not Pending","memory":"4.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}
package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfSubtree(root *TreeNode) int {
	_, _, answer := getAverage(root)
	return answer
}

func getAverage(root *TreeNode) (int, int, int) {
	if root == nil {
		return 0, 0, 0
	}
	sum, count, validNodes := root.Val, 1, 0
	leftSum, leftCount, leftValidNodes := getAverage(root.Left)
	rightSum, rightCount, rightValidNodes := getAverage(root.Right)
	validNodes += leftValidNodes + rightValidNodes
	sum += leftSum + rightSum
	count += leftCount + rightCount
	if sum/count == root.Val {
		validNodes += 1
	}
	return sum, count, validNodes
}
