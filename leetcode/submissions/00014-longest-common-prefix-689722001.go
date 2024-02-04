// Submission title: for Longest Common Prefix
// Submission url  : https://leetcode.com/submissions/detail/689722001/
// Submission json : {"id": 689722001, "status_display": "Accepted", "lang": "golang", "question_id": 14, "title_slug": "longest-common-prefix", "code": "\nimport \"fmt\"\n\n\nfunc substrings(input string) map[string]bool {\n\tresults := make(map[string]bool)\n\tfor index := range input {\n\t\tresults[string(input[0:index+1])] = true\n\t}\n\treturn results\n}\n\nfunc string_in_maps(\n\tsource map[string]bool,\n\ttarget map[string]bool,\n\tresults map[string]bool) {\n\tfor string := range source {\n\t\tif result, exists_in_results := results[string]; exists_in_results && !result {\n\t\t\tcontinue\n\t\t}\n\t\t_, exists_in_target := target[string]\n\t\tresults[string] = exists_in_target\n\t}\n}\n\nfunc longestCommonPrefix(strings []string) (result string) {\n\tresults := make(map[string]bool)\n\tprevious := make(map[string]bool)\n\tfor index, string := range strings {\n\t\tcurrent := substrings(string)\n\t\tif index == 0 {\n\t\t\tprevious = current\n\t\t}\n\t\tstring_in_maps(current, previous, results)\n\t\tstring_in_maps(previous, current, results)\n\t\tfmt.Println(\"current string\", string, current, \"results\", results)\n\t\tprevious = current\n\t}\n\tfor string, valid := range results {\n\t\tif !valid || len(string) < len(result) {\n\t\t\tcontinue\n\t\t}\n\t\tif len(string) == len(result) && string < result {\n\t\t\tresult = string\n\t\t\tcontinue\n\t\t}\n\t\tresult = string\n\t}\n\tfmt.Println(\"result\", result)\n\treturn\n}\n\n", "title": "Longest Common Prefix", "url": "/submissions/detail/689722001/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651244941, "status": 10, "runtime": "86 ms", "is_pending": "Not Pending", "memory": "6.9 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

import "fmt"

func substrings(input string) map[string]bool {
	results := make(map[string]bool)
	for index := range input {
		results[string(input[0:index+1])] = true
	}
	return results
}

func string_in_maps(
	source map[string]bool,
	target map[string]bool,
	results map[string]bool) {
	for string := range source {
		if result, exists_in_results := results[string]; exists_in_results && !result {
			continue
		}
		_, exists_in_target := target[string]
		results[string] = exists_in_target
	}
}

func longestCommonPrefix(strings []string) (result string) {
	results := make(map[string]bool)
	previous := make(map[string]bool)
	for index, string := range strings {
		current := substrings(string)
		if index == 0 {
			previous = current
		}
		string_in_maps(current, previous, results)
		string_in_maps(previous, current, results)
		fmt.Println("current string", string, current, "results", results)
		previous = current
	}
	for string, valid := range results {
		if !valid || len(string) < len(result) {
			continue
		}
		if len(string) == len(result) && string < result {
			result = string
			continue
		}
		result = string
	}
	fmt.Println("result", result)
	return
}
