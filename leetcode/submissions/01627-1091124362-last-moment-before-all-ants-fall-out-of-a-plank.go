// Submission title: Last Moment Before All Ants Fall Out of a Plank
// Submission url  : https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/"
// Submission url  : https://leetcode.com/submissions/detail/1091124362/"
package submissions

func getLastMoment(n int, left []int, right []int) int {
	maxLeft := 0
	for _, val := range left {
		if val > maxLeft {
			maxLeft = val
		}
	}

	minRight := n
	for _, val := range right {
		if val < minRight {
			minRight = val
		}
	}
	return max(maxLeft, n-minRight)
}
