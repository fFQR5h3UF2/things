// Submission title: Average Salary Excluding the Minimum and Maximum Salary
// Submission url  : https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
// Submission url  : https://leetcode.com/submissions/detail/691613273/
// Submission json : {"id":691613273,"status_display":"Accepted","lang":"golang","question_id":1584,"title_slug":"average-salary-excluding-the-minimum-and-maximum-salary","code":"\nfunc average(salary []int) float64 {\n\tlength := len(salary)\n\thighest, lowest := math.MinInt, math.MaxInt\n\tresult := 0\n\tfor _, number := range salary {\n\t\tresult += number\n\t\tif number > highest {\n\t\t\thighest = number\n\t\t}\n\t\tif number < lowest {\n\t\t\tlowest = number\n\t\t}\n\t}\n\treturn float64(result-highest-lowest) / float64(length-2)\n}\n","title":"Average Salary Excluding the Minimum and Maximum Salary","url":"/submissions/detail/691613273/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651498535,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"2 MB","compare_result":"1111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func average(salary []int) float64 {
	length := len(salary)
	highest, lowest := math.MinInt, math.MaxInt
	result := 0
	for _, number := range salary {
		result += number
		if number > highest {
			highest = number
		}
		if number < lowest {
			lowest = number
		}
	}
	return float64(result-highest-lowest) / float64(length-2)
}
