// Submission for Determine if a Cell Is Reachable at a Given Time
// Submission url: https://leetcode.com/submissions/detail/1094275272/

package submissions

func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
    vert := abs(sy, fy)
    return vert + max(0, abs(sx, fx) - vert)  <= t
}

func abs(x, y int) int {
    if x > y {
        return x - y
    }
    return y - x
}
