// Submission title: for Find the Winner of an Array Game
// Submission url  : https://leetcode.com/submissions/detail/1091924184/
// Submission json : {"id": 1091924184, "status_display": "Accepted", "lang": "golang", "question_id": 1657, "title_slug": "find-the-winner-of-an-array-game", "code": "func getWinner(arr []int, k int) int {\n    if k == 1 {\n        return max(arr[0], arr[1])\n    }\n    length := len(arr)\n    if k >= length {\n        return slices.Max(arr)\n    }\n    curWinner, winCount := arr[0], 0\n    for _, num := range arr[1:] {\n        if curWinner > num {\n            winCount++\n        } else {\n            curWinner = num\n            winCount = 1\n        }\n        if winCount == k {\n            return curWinner\n        }\n    }\n    return curWinner\n}", "title": "Find the Winner of an Array Game", "url": "/submissions/detail/1091924184/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699175163, "status": 10, "runtime": "79 ms", "is_pending": "Not Pending", "memory": "8.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func getWinner(arr []int, k int) int {
	if k == 1 {
		return max(arr[0], arr[1])
	}
	length := len(arr)
	if k >= length {
		return slices.Max(arr)
	}
	curWinner, winCount := arr[0], 0
	for _, num := range arr[1:] {
		if curWinner > num {
			winCount++
		} else {
			curWinner = num
			winCount = 1
		}
		if winCount == k {
			return curWinner
		}
	}
	return curWinner
}
