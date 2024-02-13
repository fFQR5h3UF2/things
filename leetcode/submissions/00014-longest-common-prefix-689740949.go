// Submission title: Longest Common Prefix
// Submission url  : https://leetcode.com/problems/longest-common-prefix/description/
// Submission url  : https://leetcode.com/submissions/detail/689740949/
// Submission json : {"id":689740949,"status_display":"Accepted","lang":"golang","question_id":14,"title_slug":"longest-common-prefix","code":"\nfunc substrings(input string) map[string]bool {\n\tresults := make(map[string]bool)\n\tfor index := range input {\n\t\tresults[input[0:index+1]] = true\n\t}\n\treturn results\n}\n\nfunc string_in_maps(\n\tsource map[string]bool,\n\ttarget map[string]bool,\n\tresults map[string]bool) {\n\tfor string := range source {\n\t\tis_valid, exists_in_results := results[string]\n\t\t_, exists_in_target := target[string]\n\t\tswitch {\n\t\tcase !exists_in_target:\n\t\t\tfallthrough\n\t\tcase exists_in_target && (is_valid || !exists_in_results):\n\t\t\tresults[string] = exists_in_target\n\t\t}\n\t}\n}\n\nfunc longestCommonPrefix(strings []string) (result string) {\n\tresults := make(map[string]bool)\n\tvar previous map[string]bool\n\tfor index, string := range strings {\n\t\tcurrent := substrings(string)\n\t\tif index == 0 {\n\t\t\tprevious = current\n\t\t}\n\t\tstring_in_maps(previous, current, results)\n\t\tstring_in_maps(current, previous, results)\n\t\tprevious = current\n\t}\n\tfor string, valid := range results {\n\t\tif valid && len(string) > len(result) {\n\t\t\tresult = string\n\t\t}\n\t}\n\treturn\n}\n\n","title":"Longest Common Prefix","url":"/submissions/detail/689740949/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651247464,"status":10,"runtime":"33 ms","is_pending":"Not Pending","memory":"6.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func substrings(input string) map[string]bool {
	results := make(map[string]bool)
	for index := range input {
		results[input[0:index+1]] = true
	}
	return results
}

func string_in_maps(
	source map[string]bool,
	target map[string]bool,
	results map[string]bool) {
	for string := range source {
		is_valid, exists_in_results := results[string]
		_, exists_in_target := target[string]
		switch {
		case !exists_in_target:
			fallthrough
		case exists_in_target && (is_valid || !exists_in_results):
			results[string] = exists_in_target
		}
	}
}

func longestCommonPrefix(strings []string) (result string) {
	results := make(map[string]bool)
	var previous map[string]bool
	for index, string := range strings {
		current := substrings(string)
		if index == 0 {
			previous = current
		}
		string_in_maps(previous, current, results)
		string_in_maps(current, previous, results)
		previous = current
	}
	for string, valid := range results {
		if valid && len(string) > len(result) {
			result = string
		}
	}
	return
}
