// Submission title: for Squares of a Sorted Array
// Submission url  : https://leetcode.com/submissions/detail/692273896/
// Submission json : {"id": 692273896, "status_display": "Accepted", "lang": "golang", "question_id": 1019, "title_slug": "squares-of-a-sorted-array", "code": "\nfunc sortedSquares(numbers []int) []int {\n\tlength := len(numbers)\n\tswitch length {\n\tcase 0:\n\t\treturn numbers\n\tcase 1:\n\t\treturn []int{numbers[0] * numbers[0]}\n\t}\n\tindex_left, index_right := 0, length-1\n\tresults := make([]int, length)\n\tfor index := index_right; index_left <= index_right; index-- {\n\t\tleft_square := numbers[index_left] * numbers[index_left]\n\t\tright_square := numbers[index_right] * numbers[index_right]\n\t\tif right_square > left_square {\n\t\t\tresults[index] = right_square\n\t\t\tindex_right--\n\t\t\tcontinue\n\t\t}\n\t\tresults[index] = left_square\n\t\tindex_left++\n\t}\n\treturn results\n}\n", "title": "Squares of a Sorted Array", "url": "/submissions/detail/692273896/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651579502, "status": 10, "runtime": "60 ms", "is_pending": "Not Pending", "memory": "7.2 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func sortedSquares(numbers []int) []int {
	length := len(numbers)
	switch length {
	case 0:
		return numbers
	case 1:
		return []int{numbers[0] * numbers[0]}
	}
	index_left, index_right := 0, length-1
	results := make([]int, length)
	for index := index_right; index_left <= index_right; index-- {
		left_square := numbers[index_left] * numbers[index_left]
		right_square := numbers[index_right] * numbers[index_right]
		if right_square > left_square {
			results[index] = right_square
			index_right--
			continue
		}
		results[index] = left_square
		index_left++
	}
	return results
}
