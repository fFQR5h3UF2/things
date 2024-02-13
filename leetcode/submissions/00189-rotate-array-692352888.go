// Submission title: Rotate Array
// Submission url  : https://leetcode.com/problems/rotate-array/description/
// Submission url  : https://leetcode.com/submissions/detail/692352888/
// Submission json : {"id":692352888,"status_display":"Accepted","lang":"golang","question_id":189,"title_slug":"rotate-array","code":"\nfunc rotate(numbers []int, steps int) {\n\tlength := len(numbers)\n\t// removing unnecessary steps\n\tif steps >= length {\n\t\tsteps %= length\n\t}\n\t// checking edge cases\n\tif length == 1 || steps == 0 {\n\t\treturn\n\t}\n\tresults := make([]int, length)\n\tfor index, number := range numbers {\n\t\tresults[(index+steps)%length] = number\n\t}\n\tcopy(numbers, results)\n}","title":"Rotate Array","url":"/submissions/detail/692352888/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651588797,"status":10,"runtime":"79 ms","is_pending":"Not Pending","memory":"8.6 MB","compare_result":"11111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func rotate(numbers []int, steps int) {
	length := len(numbers)
	// removing unnecessary steps
	if steps >= length {
		steps %= length
	}
	// checking edge cases
	if length == 1 || steps == 0 {
		return
	}
	results := make([]int, length)
	for index, number := range numbers {
		results[(index+steps)%length] = number
	}
	copy(numbers, results)
}
