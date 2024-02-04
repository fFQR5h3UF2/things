// Submission for Last Moment Before All Ants Fall Out of a Plank
// Submission url: https://leetcode.com/submissions/detail/1091124362/

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
    return max(maxLeft, n - minRight)
}
