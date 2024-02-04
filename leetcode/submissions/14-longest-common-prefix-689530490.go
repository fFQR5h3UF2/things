// Submission for Longest Common Prefix
// Submission url: https://leetcode.com/submissions/detail/689530490/

package submissions

import "fmt"

// https://leetcode.com/problems/longest-common-prefix/

func substrings(input string) map[string]bool {
	results := make(map[string]bool)
	for index := range input {
		results[string(input[index])] = true
		for index_inner := index; index_inner <= len(input); index_inner++ {
			results[input[index:index_inner]] = true
		}
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
