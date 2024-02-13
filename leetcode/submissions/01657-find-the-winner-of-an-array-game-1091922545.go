// Submission title: Find the Winner of an Array Game
// Submission url  : https://leetcode.com/problems/find-the-winner-of-an-array-game/description/
// Submission url  : https://leetcode.com/submissions/detail/1091922545/
// Submission json : {"id":1091922545,"status_display":"Accepted","lang":"golang","question_id":1657,"title_slug":"find-the-winner-of-an-array-game","code":"func getWinner(arr []int, k int) int {\n    curMax, winCount := arr[0], 0\n    i, length := 1, len(arr)\n    for {\n        num := arr[i]\n        if num > curMax {\n            curMax = num\n            winCount = 1\n        } else {\n            winCount++\n        }\n        if winCount == k {\n            return curMax\n        }\n        i = (i + 1) % length\n    }\n    return -1\n}","title":"Find the Winner of an Array Game","url":"/submissions/detail/1091922545/","lang_name":"Go","time":"3 months","timestamp":1699174919,"status":10,"runtime":"3261 ms","is_pending":"Not Pending","memory":"11.1 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func getWinner(arr []int, k int) int {
	curMax, winCount := arr[0], 0
	i, length := 1, len(arr)
	for {
		num := arr[i]
		if num > curMax {
			curMax = num
			winCount = 1
		} else {
			winCount++
		}
		if winCount == k {
			return curMax
		}
		i = (i + 1) % length
	}
	return -1
}
