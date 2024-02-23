// Submission title: Determine if a Cell Is Reachable at a Given Time
// Submission url  : https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description/
// Submission url  : https://leetcode.com/submissions/detail/1094276079/"
package submissions

func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
	vert := abs(sy, fy)
	dist := vert + max(0, abs(sx, fx)-vert)
	if dist == 0 && t == 1 {
		return false
	}
	return dist <= t
}

func abs(x, y int) int {
	if x > y {
		return x - y
	}
	return y - x
}
