// Submission for Last Moment Before All Ants Fall Out of a Plank
// Submission url: https://leetcode.com/submissions/detail/1091126622/

package submissions

func getLastMoment(n int, left []int, right []int) int {
    return max(slices.Left(append(left, 0)), n - slices.Min(append(right, n)))
}
