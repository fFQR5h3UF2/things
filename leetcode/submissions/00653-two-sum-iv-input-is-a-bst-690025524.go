// Submission title: Two Sum IV - Input is a BST
// Submission url  : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
// Submission url  : https://leetcode.com/submissions/detail/690025524/
// Submission json : {"id":690025524,"status_display":"Accepted","lang":"golang","question_id":653,"title_slug":"two-sum-iv-input-is-a-bst","code":"\nfunc construct(root *TreeNode, results map[int]int) {\n\tif root == nil {\n\t\treturn\n\t}\n\tif results[root.Val] < 2 {\n\t\tresults[root.Val] += 1\n\t}\n\tconstruct(root.Left, results)\n\tconstruct(root.Right, results)\n}\n\nfunc findTarget(root *TreeNode, target int) bool {\n\tresults := map[int]int{}\n\tconstruct(root, results)\n\tfor number, count := range results {\n\t\tif count == 2 && number*2 == target {\n\t\t\treturn true\n\t\t}\n\t\tfor number_inner := range results {\n\t\t\tif number_inner <= number {\n\t\t\t\tcontinue\n\t\t\t}\n\t\t\tif number+number_inner == target {\n\t\t\t\treturn true\n\t\t\t}\n\t\t}\n\t}\n\treturn false\n}","title":"Two Sum IV - Input is a BST","url":"/submissions/detail/690025524/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651294326,"status":10,"runtime":"73 ms","is_pending":"Not Pending","memory":"7.9 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
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
