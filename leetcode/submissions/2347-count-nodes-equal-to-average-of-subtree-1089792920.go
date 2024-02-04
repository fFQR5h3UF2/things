// Submission for Count Nodes Equal to Average of Subtree
// Submission url: https://leetcode.com/submissions/detail/1089792920/

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
    _, answer := getAverage(root)
    return answer
}

func getAverage(root *TreeNode) (int, int) {
    if root == nil {
        return 0, 0
    }
    average, validNodes := root.Val, 0
    if root.Left != nil {
        leftAverage, leftValidNodes := getAverage(root.Left)
        validNodes += leftValidNodes
        average = (average + leftAverage) / 2
    }
    if root.Right != nil {
        rightAverage, rightValidNodes := getAverage(root.Right)
        validNodes += rightValidNodes
        average = (average + rightAverage) / 2
    }
    if average == root.Val {
        validNodes += 1
    }
    return average, validNodes
}
