// Submission title: for Determine if a Cell Is Reachable at a Given Time
// Submission url  : https://leetcode.com/submissions/detail/1094276079/
// Submission json : {"id": 1094276079, "status_display": "Accepted", "lang": "golang", "question_id": 3056, "title_slug": "determine-if-a-cell-is-reachable-at-a-given-time", "code": "func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {\n    vert := abs(sy, fy)\n    dist := vert + max(0, abs(sx, fx) - vert)\n    if dist == 0 && t == 1 {\n        return false\n    }\n    return dist <= t\n}\n\nfunc abs(x, y int) int {\n    if x > y {\n        return x - y\n    }\n    return y - x\n}", "title": "Determine if a Cell Is Reachable at a Given Time", "url": "/submissions/detail/1094276079/", "lang_name": "Go", "time": "2\u00a0months, 4\u00a0weeks", "timestamp": 1699430941, "status": 10, "runtime": "5 ms", "is_pending": "Not Pending", "memory": "2.6 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

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
