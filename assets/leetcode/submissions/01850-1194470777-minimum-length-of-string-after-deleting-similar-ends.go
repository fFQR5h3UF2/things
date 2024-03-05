// Submission title: Minimum Length of String After Deleting Similar Ends
// Submission url  : https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/
// Submission url  : https://leetcode.com/submissions/detail/1194470777/"
package submissions

func minimumLength(s string) int {
	left := 0
	right := len(s) - 1

	for left < right {
		lc := s[left]
		rc := s[right]

		if lc != rc {
			return right - left + 1
		}

		for left+1 < right && lc == s[left+1] {
			left++
		}

		for left < right-1 && rc == s[right-1] {
			right--
		}

		right--
		left++
	}

	return right - left + 1
}
