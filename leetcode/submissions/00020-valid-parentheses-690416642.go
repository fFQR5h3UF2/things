// Submission title: Valid Parentheses
// Submission url  : https://leetcode.com/problems/valid-parentheses/description/
// Submission url  : https://leetcode.com/submissions/detail/690416642/
// Submission json : {"id":690416642,"status_display":"Accepted","lang":"golang","question_id":20,"title_slug":"valid-parentheses","code":"\nfunc isValid(inputString string) bool {\n\tif len(inputString) == 0 || (len(inputString)&1) != 0 {\n\t\treturn false\n\t}\n\toccurences := []rune{}\n\tends := map[rune]rune{')': '(', '}': '{', ']': '['}\n\tfor _, character := range inputString {\n\t\tlength := len(occurences)\n\t\tlast_valid, is_end := ends[character]\n\t\tif (is_end && length == 0) || (is_end && occurences[length-1] != last_valid) {\n\t\t\treturn false\n\t\t}\n\t\tif is_end {\n\t\t\toccurences = occurences[0 : length-1]\n\t\t} else {\n\t\t\toccurences = append(occurences, character)\n\t\t}\n\t}\n\tif len(occurences) > 0 {\n\t\treturn false\n\t}\n\treturn true\n}\n","title":"Valid Parentheses","url":"/submissions/detail/690416642/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651345571,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"2.1 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func isValid(inputString string) bool {
	if len(inputString) == 0 || (len(inputString)&1) != 0 {
		return false
	}
	occurences := []rune{}
	ends := map[rune]rune{')': '(', '}': '{', ']': '['}
	for _, character := range inputString {
		length := len(occurences)
		last_valid, is_end := ends[character]
		if (is_end && length == 0) || (is_end && occurences[length-1] != last_valid) {
			return false
		}
		if is_end {
			occurences = occurences[0 : length-1]
		} else {
			occurences = append(occurences, character)
		}
	}
	if len(occurences) > 0 {
		return false
	}
	return true
}
