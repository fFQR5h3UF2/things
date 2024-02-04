// Submission title: for Two Sum IV - Input is a BST
// Submission url  : https://leetcode.com/submissions/detail/690048286/
// Submission json : {"id": 690048286, "status_display": "Accepted", "lang": "golang", "question_id": 653, "title_slug": "two-sum-iv-input-is-a-bst", "code": "import \"sort\"\nfunc construct(root *TreeNode, results map[int]int) {\n\tif root == nil {\n\t\treturn\n\t}\n\tif results[root.Val] < 2 {\n\t\tresults[root.Val] += 1\n\t}\n\tconstruct(root.Left, results)\n\tconstruct(root.Right, results)\n}\n\nfunc sorted(input_map map[int]int) (results []int) {\n\tfor key := range input_map {\n\t\tresults = append(results, key)\n\t}\n\treturn\n}\n\nfunc findTarget(root *TreeNode, target int) bool {\n\tif root == nil {\n\t\treturn false\n\t}\n\tresults := map[int]int{}\n\tconstruct(root, results)\n\tif target%2 == 0 && results[target/2] == 2 {\n\t\treturn true\n\t}\n\tresults_sorted := sorted(results)\n\tresults_sorted_len := len(results_sorted)\n\tsort.Ints(results_sorted)\n\tfor index, number := range results_sorted {\n\t\tfor index_inner := index + 1; index_inner < results_sorted_len; index_inner++ {\n\t\t\tif number+results_sorted[index_inner] == target {\n\t\t\t\treturn true\n\t\t\t}\n\t\t}\n\t}\n\treturn false\n}", "title": "Two Sum IV - Input is a BST", "url": "/submissions/detail/690048286/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651297787, "status": 10, "runtime": "35 ms", "is_pending": "Not Pending", "memory": "7.8 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

import "sort"

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

func sorted(input_map map[int]int) (results []int) {
	for key := range input_map {
		results = append(results, key)
	}
	return
}

func findTarget(root *TreeNode, target int) bool {
	if root == nil {
		return false
	}
	results := map[int]int{}
	construct(root, results)
	if target%2 == 0 && results[target/2] == 2 {
		return true
	}
	results_sorted := sorted(results)
	results_sorted_len := len(results_sorted)
	sort.Ints(results_sorted)
	for index, number := range results_sorted {
		for index_inner := index + 1; index_inner < results_sorted_len; index_inner++ {
			if number+results_sorted[index_inner] == target {
				return true
			}
		}
	}
	return false
}
