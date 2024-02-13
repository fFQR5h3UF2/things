// Submission title: Largest Perimeter Triangle
// Submission url  : https://leetcode.com/problems/largest-perimeter-triangle/description/
// Submission url  : https://leetcode.com/submissions/detail/692736039/
// Submission json : {"id":692736039,"status_display":"Accepted","lang":"golang","question_id":1018,"title_slug":"largest-perimeter-triangle","code":"\nfunc largestPerimeter(numbers []int) int {\n\tsort.Ints(numbers)\n\tfor index := len(numbers) - 1; index > 1; index-- {\n\t\tcurrent, sum_previous := numbers[index], numbers[index-1]+numbers[index-2]\n\t\tif current >= sum_previous {\n\t\t\tcontinue\n\t\t}\n\t\treturn current + sum_previous\n\t}\n\treturn 0\n}","title":"Largest Perimeter Triangle","url":"/submissions/detail/692736039/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651635568,"status":10,"runtime":"57 ms","is_pending":"Not Pending","memory":"6.9 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func largestPerimeter(numbers []int) int {
	sort.Ints(numbers)
	for index := len(numbers) - 1; index > 1; index-- {
		current, sum_previous := numbers[index], numbers[index-1]+numbers[index-2]
		if current >= sum_previous {
			continue
		}
		return current + sum_previous
	}
	return 0
}
