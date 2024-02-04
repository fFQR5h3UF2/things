// Submission for Valid Parentheses
// Submission url: https://leetcode.com/submissions/detail/690410694/

package submissions


func isValid(inputString string) bool {
	if len(inputString) == 0 || (len(inputString)&1) != 0 {
		return false
	}
	occurences := make([]rune, len(inputString))
	ends := map[rune]rune{')': '(', '}': '{', ']': '['}
	for _, character := range inputString {
		length := len(occurences)
		last := occurences[length-1]
		last_valid, is_end := ends[character]
		if is_end && last != last_valid {
			return false
		}
		if is_end {
			occurences = occurences[0 : length-2]
		} else {
			occurences = append(occurences, character)
		}
	}
	return true
}
