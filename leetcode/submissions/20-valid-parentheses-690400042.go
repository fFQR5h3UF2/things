// Submission for Valid Parentheses
// Submission url: https://leetcode.com/submissions/detail/690400042/

package submissions


func isValid(inputString string) bool {
	occurences := map[rune]bool{'(': false, ')': false, '{': false, '}': false, '[': false, ']': false}
	ends := map[rune]rune{')': '(', '}': '{', ']': '['}
	for _, character := range inputString {
		if start, is_end := ends[character]; is_end {
			valid := check(occurences, start, character)
			if !valid {
				return false
			}
			continue
		}
		appearedBefore := occurences[character]
		if appearedBefore {
			return false
		}
		occurences[character] = true
	}
	for _, notClosed := range occurences {
		if notClosed {
			return false
		}
	}
	return true
}

func check(brackets map[rune]bool, start rune, end rune) bool {
	if !brackets[start] || brackets[end] {
		return false
	}
	brackets[start], brackets[end] = false, false
	return true
}
