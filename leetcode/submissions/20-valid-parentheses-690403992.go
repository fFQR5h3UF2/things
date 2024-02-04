// Submission for Valid Parentheses
// Submission url: https://leetcode.com/submissions/detail/690403992/

package submissions


func isValid(inputString string) bool {
	ends := map[rune]rune{')': '(', '}': '{', ']': '['}
	length := len(inputString)
	if length < 2 || (length&1) != 0 {
		return false
	}
	for index := 1; index < len(inputString); index += 2 {
		if ends[rune(inputString[index])] != rune(inputString[index-1]) {
			return false
		}
	}
	return true
}
