// Submission title: Minimum Number of Arrows to Burst Balloons
// Submission url  : https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/
// Submission url  : https://leetcode.com/submissions/detail/1091199566/
// Submission json : {"id":1091199566,"status_display":"Accepted","lang":"golang","question_id":452,"title_slug":"minimum-number-of-arrows-to-burst-balloons","code":"func findMinArrowShots(points [][]int) int {\n\t// greedy solution\n\tsort.Slice(points, func(i, j int) bool {\n\t\treturn points[i][1] < points[j][1]\n\t})\n\tcount := 1\n\tend := points[0][1]\n\tfor i := 1; i < len(points); i++ {\n\t\tif points[i][0] > end {\n\t\t\tcount++\n\t\t\tend = points[i][1]\n\t\t}\n\t}\n\treturn count\n}","title":"Minimum Number of Arrows to Burst Balloons","url":"/submissions/detail/1091199566/","lang_name":"Go","time":"3 months","timestamp":1699093541,"status":10,"runtime":"204 ms","is_pending":"Not Pending","memory":"17.1 MB","compare_result":"11111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func findMinArrowShots(points [][]int) int {
	// greedy solution
	sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})
	count := 1
	end := points[0][1]
	for i := 1; i < len(points); i++ {
		if points[i][0] > end {
			count++
			end = points[i][1]
		}
	}
	return count
}
