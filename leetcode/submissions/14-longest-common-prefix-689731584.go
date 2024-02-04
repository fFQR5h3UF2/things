// Submission for Longest Common Prefix
// Submission url: https://leetcode.com/submissions/detail/689731584/

package submissions

package main

// https://leetcode.com/problems/longest-common-prefix/

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
		_, exists_in_results := results[string]
		_, exists_in_target := target[string]
		if !exists_in_target {
			delete(results, string)
		} else if !exists_in_results && exists_in_target {
			results[string] = exists_in_target
		}
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

		previous = current
	}
	for string := range results {
		if len(string) > len(result) {
			result = string
		}
	}
	return
}
