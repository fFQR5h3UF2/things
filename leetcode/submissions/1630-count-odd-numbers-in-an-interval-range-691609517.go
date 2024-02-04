// Submission for Count Odd Numbers in an Interval Range
// Submission url: https://leetcode.com/submissions/detail/691609517/

package submissions


func countOdds(low int, high int) int {
	if low == 0 {
		return high / 2
	} else if high == 0 {
		return low / 2
	}
	low_even, high_even, half := (low&1) == 0, (high&1) == 0, (high-low)/2
	if low_even && high_even  {
		return half
	}
	return half + 1
}
