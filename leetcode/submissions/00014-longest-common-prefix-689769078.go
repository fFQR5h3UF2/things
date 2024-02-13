// Submission title: Longest Common Prefix
// Submission url  : https://leetcode.com/problems/longest-common-prefix/description/
// Submission url  : https://leetcode.com/submissions/detail/689769078/
// Submission json : {"id":689769078,"status_display":"Accepted","lang":"golang","question_id":14,"title_slug":"longest-common-prefix","code":"func longestCommonPrefix(strings []string) string {\n\tswitch len(strings) {\n\tcase 0:\n\t\treturn \"\"\n\tcase 1:\n\t\treturn strings[0]\n\t}\n\tresult := strings[0]\nfor index := 1; index < len(strings); index++ {\n\t\tcurrent := strings[index]\n\t\tprevious := strings[index-1]\n\t\tcurrent_max := len(current)\n\t\tresult_max := len(result)\n\t\tvar slice_max int\n\t\tif result_max > current_max {\n\t\t\tslice_max = current_max\n\t\t\tresult = result[0:slice_max]\n\t\t} else {\n\t\t\tslice_max = result_max\n\t\t}\n\t\tfor ; slice_max >= 0; slice_max-- {\n\t\t\tcurrent_slice := current[0:slice_max]\n\t\t\tif current_slice == previous[0:slice_max] {\n\t\t\t\tresult = current_slice\n\t\t\t\tbreak\n\t\t\t}\n\t\t\tif slice_max == 0 {\n\t\t\t\treturn \"\"\n\t\t\t}\n\t\t}\n\t}\t\n    return result\n}","title":"Longest Common Prefix","url":"/submissions/detail/689769078/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651251166,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"2.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func longestCommonPrefix(strings []string) string {
	switch len(strings) {
	case 0:
		return ""
	case 1:
		return strings[0]
	}
	result := strings[0]
	for index := 1; index < len(strings); index++ {
		current := strings[index]
		previous := strings[index-1]
		current_max := len(current)
		result_max := len(result)
		var slice_max int
		if result_max > current_max {
			slice_max = current_max
			result = result[0:slice_max]
		} else {
			slice_max = result_max
		}
		for ; slice_max >= 0; slice_max-- {
			current_slice := current[0:slice_max]
			if current_slice == previous[0:slice_max] {
				result = current_slice
				break
			}
			if slice_max == 0 {
				return ""
			}
		}
	}
	return result
}
