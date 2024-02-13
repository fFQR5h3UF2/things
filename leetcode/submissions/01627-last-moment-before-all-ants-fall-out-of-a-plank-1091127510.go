// Submission title: Last Moment Before All Ants Fall Out of a Plank
// Submission url  : https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/description/
// Submission url  : https://leetcode.com/submissions/detail/1091127510/
// Submission json : {"id":1091127510,"status_display":"Accepted","lang":"golang","question_id":1627,"title_slug":"last-moment-before-all-ants-fall-out-of-a-plank","code":"\nfunc getLastMoment(n int, left []int, right []int) int {\n    return max(slices.Max(append(left, 0)), n - slices.Min(append(right, n)))\n}","title":"Last Moment Before All Ants Fall Out of a Plank","url":"/submissions/detail/1091127510/","lang_name":"Go","time":"3 months","timestamp":1699083377,"status":10,"runtime":"19 ms","is_pending":"Not Pending","memory":"6.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func getLastMoment(n int, left []int, right []int) int {
	return max(slices.Max(append(left, 0)), n-slices.Min(append(right, n)))
}
