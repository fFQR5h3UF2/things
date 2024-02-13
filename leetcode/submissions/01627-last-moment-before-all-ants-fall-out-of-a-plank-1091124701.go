// Submission title: Last Moment Before All Ants Fall Out of a Plank
// Submission url  : https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/
// Submission url  : https://leetcode.com/submissions/detail/1091124701/
// Submission json : {"id":1091124701,"status_display":"Accepted","lang":"golang","question_id":1627,"title_slug":"last-moment-before-all-ants-fall-out-of-a-plank","code":"func getLastMoment(n int, left []int, right []int) int {\n    maxLeft := 0\n    for _, val := range left {\n        if val > maxLeft {\n            maxLeft = val\n        }\n    }\n    minRight := n\n    for _, val := range right {\n        if val < minRight {\n            minRight = val\n        }\n    }\n    return max(maxLeft, n - minRight)\n}","title":"Last Moment Before All Ants Fall Out of a Plank","url":"/submissions/detail/1091124701/","lang_name":"Go","time":"3 months","timestamp":1699083011,"status":10,"runtime":"16 ms","is_pending":"Not Pending","memory":"6.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
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
