// Submission title: Last Moment Before All Ants Fall Out of a Plank
// Submission url  : https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/
// Submission url  : https://leetcode.com/submissions/detail/1091127510/"
package submissions

func getLastMoment(n int, left []int, right []int) int {
	return max(slices.Max(append(left, 0)), n-slices.Min(append(right, n)))
}
