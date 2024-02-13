// Submission title: Insert Interval
// Submission url  : https://leetcode.com/problems/insert-interval/description/
// Submission url  : https://leetcode.com/submissions/detail/1091198577/
// Submission json : {"id":1091198577,"status_display":"Accepted","lang":"golang","question_id":57,"title_slug":"insert-interval","code":"func insert(intervals [][]int, new []int) [][]int {\n    n := len(intervals)\n    i := sort.Search(n, func(i int) bool { return intervals[i][0] > new[0] })\n    j := sort.Search(n, func(j int) bool { return intervals[j][1] > new[1] })\n    if i >= 1 && new[0] <= intervals[i-1][1] {\n        new[0] = intervals[i-1][0]\n        i--\n    }\n    if j < n && new[1] >= intervals[j][0] {\n        new[1] = intervals[j][1]\n        j++\n    }\n    return append(intervals[:i], append([][]int{new}, intervals[j:]...)...)\n}","title":"Insert Interval","url":"/submissions/detail/1091198577/","lang_name":"Go","time":"3 months","timestamp":1699093410,"status":10,"runtime":"7 ms","is_pending":"Not Pending","memory":"4.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func insert(intervals [][]int, new []int) [][]int {
	n := len(intervals)
	i := sort.Search(n, func(i int) bool { return intervals[i][0] > new[0] })
	j := sort.Search(n, func(j int) bool { return intervals[j][1] > new[1] })
	if i >= 1 && new[0] <= intervals[i-1][1] {
		new[0] = intervals[i-1][0]
		i--
	}
	if j < n && new[1] >= intervals[j][0] {
		new[1] = intervals[j][1]
		j++
	}
	return append(intervals[:i], append([][]int{new}, intervals[j:]...)...)
}
