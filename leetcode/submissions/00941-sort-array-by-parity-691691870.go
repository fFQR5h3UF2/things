// Submission title: Sort Array By Parity
// Submission url  : https://leetcode.com/problems/sort-array-by-parity/description/
// Submission url  : https://leetcode.com/submissions/detail/691691870/
// Submission json : {"id":691691870,"status_display":"Accepted","lang":"golang","question_id":941,"title_slug":"sort-array-by-parity","code":"\nfunc sortArrayByParity(numbers []int) []int {\n\tlength := len(numbers)\n\tif length == 1 {\n\t\treturn numbers\n\t}\n\tresults, index_even, index_odd := make([]int, length), 0, length-1\n\tfor _, number := range numbers {\n\t\tif (number & 1) == 0 {\n\t\t\t// number is even -> place it from the beginning\n\t\t\tresults[index_even] = number\n\t\t\tindex_even++\n\t\t} else {\n\t\t\t// number is odd -> place it from the end\n\t\t\tresults[index_odd] = number\n\t\t\tindex_odd--\n\t\t}\n\t}\n\treturn results\n}\n","title":"Sort Array By Parity","url":"/submissions/detail/691691870/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651507660,"status":10,"runtime":"9 ms","is_pending":"Not Pending","memory":"5.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func sortArrayByParity(numbers []int) []int {
	length := len(numbers)
	if length == 1 {
		return numbers
	}
	results, index_even, index_odd := make([]int, length), 0, length-1
	for _, number := range numbers {
		if (number & 1) == 0 {
			// number is even -> place it from the beginning
			results[index_even] = number
			index_even++
		} else {
			// number is odd -> place it from the end
			results[index_odd] = number
			index_odd--
		}
	}
	return results
}
