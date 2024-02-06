// Submission title: for Two Sum IV - Input is a BST
// Submission url  : https://leetcode.com/submissions/detail/690047944/
// Submission json : {"id": 690047944, "status_display": "Accepted", "lang": "golang", "question_id": 653, "title_slug": "two-sum-iv-input-is-a-bst", "code": "import \"sort\"\n\nfunc construct(root *TreeNode, results map[int]bool, doubles map[int]bool) {\n\tif root == nil {\n\t\treturn\n\t}\n\t_, exists := results[root.Val]\n\tif !exists {\n\t\tresults[root.Val] = true\n\t} else if _, double := doubles[root.Val]; exists && double {\n\t\tdoubles[root.Val] = true\n\t}\n\tconstruct(root.Left, results, doubles)\n\tconstruct(root.Right, results, doubles)\n}\n\nfunc sorted(input_map map[int]bool) (results []int) {\n\tfor key := range input_map {\n\t\tresults = append(results, key)\n\t}\n\treturn\n}\n\nfunc findTarget(root *TreeNode, target int) bool {\n\tif root == nil {\n\t\treturn false\n\t}\n\tresults := map[int]bool{}\n\tdoubles := map[int]bool{}\n\tconstruct(root, results, doubles)\n\tif _, double_exists := doubles[target/2]; target%2 == 0 && double_exists {\n\t\treturn true\n\t}\n\tresults_sorted := sorted(results)\n\tresults_sorted_len := len(results_sorted)\n\tsort.Ints(results_sorted)\n\tfor index, number := range results_sorted {\n\t\tfor index_inner := index + 1; index_inner < results_sorted_len; index_inner++ {\n\t\t\tif number+results_sorted[index_inner] == target {\n\t\t\t\treturn true\n\t\t\t}\n\t\t}\n\t}\n\treturn false\n}", "title": "Two Sum IV - Input is a BST", "url": "/submissions/detail/690047944/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651297739, "status": 10, "runtime": "46 ms", "is_pending": "Not Pending", "memory": "8.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

import "sort"

func construct(root *TreeNode, results map[int]bool, doubles map[int]bool) {
	if root == nil {
		return
	}
	_, exists := results[root.Val]
	if !exists {
		results[root.Val] = true
	} else if _, double := doubles[root.Val]; exists && double {
		doubles[root.Val] = true
	}
	construct(root.Left, results, doubles)
	construct(root.Right, results, doubles)
}

func sorted(input_map map[int]bool) (results []int) {
	for key := range input_map {
		results = append(results, key)
	}
	return
}

func findTarget(root *TreeNode, target int) bool {
	if root == nil {
		return false
	}
	results := map[int]bool{}
	doubles := map[int]bool{}
	construct(root, results, doubles)
	if _, double_exists := doubles[target/2]; target%2 == 0 && double_exists {
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
