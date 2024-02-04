// Submission for Last Moment Before All Ants Fall Out of a Plank
// Submission url: https://leetcode.com/submissions/detail/1091125843/

package submissions

func getLastMoment(n int, left []int, right []int) int {
    return max(slices.Max(left), n - slices.Min(right))
}
