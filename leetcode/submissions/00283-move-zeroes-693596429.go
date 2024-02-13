// Submission title: Move Zeroes
// Submission url  : https://leetcode.com/problems/move-zeroes/description/
// Submission url  : https://leetcode.com/submissions/detail/693596429/
// Submission json : {"id":693596429,"status_display":"Accepted","lang":"golang","question_id":283,"title_slug":"move-zeroes","code":"\nfunc moveZeroes(numbers []int) {\n\t// ensure there are at least two numbers\n\tlength := len(numbers)\n\tif length == 1 {\n\t\treturn\n\t}\n\tresult, index_result := make([]int, length), 0\n\tfor _, number := range numbers {\n\t\tif number == 0 {\n\t\t\tcontinue\n\t\t}\n\t\tresult[index_result] = number\n\t\tindex_result++\n\t}\n\tcopy(numbers, result)\n}","title":"Move Zeroes","url":"/submissions/detail/693596429/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651745691,"status":10,"runtime":"26 ms","is_pending":"Not Pending","memory":"6.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func moveZeroes(numbers []int) {
	// ensure there are at least two numbers
	length := len(numbers)
	if length == 1 {
		return
	}
	result, index_result := make([]int, length), 0
	for _, number := range numbers {
		if number == 0 {
			continue
		}
		result[index_result] = number
		index_result++
	}
	copy(numbers, result)
}
