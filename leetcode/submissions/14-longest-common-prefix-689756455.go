// Submission for Longest Common Prefix
// Submission url: https://leetcode.com/submissions/detail/689756455/

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
		for length := len(result) - 1; length >= 0; length-- {
			if length > len(current)-1 {
				result = result[0:length]
			} else if current[0:length] == previous[0:length] {
				result = current[0:length]
				break
			}
		}
	}
	return result
}
