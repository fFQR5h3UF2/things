// Submission for Last Moment Before All Ants Fall Out of a Plank
// Submission url: https://leetcode.com/submissions/detail/1091125391/

package submissions

func getLastMoment(n int, left []int, right []int) int {
    return max(max(left), n - min(right))
}
