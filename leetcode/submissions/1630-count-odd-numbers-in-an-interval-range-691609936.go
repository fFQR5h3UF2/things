// Submission for Count Odd Numbers in an Interval Range
// Submission url: https://leetcode.com/submissions/detail/691609936/

package submissions

func countOdds(low int, high int) int {
	low_even, high_even, half := (low&1) == 0, (high&1) == 0, (high-low)/2
	if low_even && high_even {
		return half
	}
	return half + 1
}
