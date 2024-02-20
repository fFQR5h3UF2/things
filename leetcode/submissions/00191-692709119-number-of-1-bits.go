// Submission title: Number of 1 Bits
// Submission url  : https://leetcode.com/problems/number-of-1-bits/description/
// Submission url  : https://leetcode.com/submissions/detail/692709119/"
package submissions

func hammingWeight(number uint32) (result int) {
	for number > 0 {
		if number&1 != 0 {
			result++
		}
		number >>= 1
	}
	return
}
