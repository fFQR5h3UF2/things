// Submission title: Find Palindrome With Fixed Length
// Submission url  : https://leetcode.com/problems/find-palindrome-with-fixed-length/description/"
// Submission url  : https://leetcode.com/submissions/detail/690364689/"
package submissions

func kthPalindrome(queries []int, intLength int) (answer []int64) {
	for _, query := range queries {
		answer = append(answer, getPalindrom(query, intLength))
	}
	return
}

func getPalindrom(query int, length int) (result int64) {
	is_even := (length & 1) == 0
	power := length / 2
	if is_even {
		power -= 1
	}
	palindrome := int64(math.Pow10(power)) + int64(query) - 1
	result = palindrome
	if !is_even {
		palindrome /= 10
	}
	for palindrome > 0 {
		result = result*10 + palindrome%10
		palindrome /= 10
	}
	if len(fmt.Sprint(result)) != length {
		return -1
	}
	return
}
