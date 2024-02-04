// Submission title: for Two Sum
// Submission url  : https://leetcode.com/submissions/detail/692799105/
// Submission json : {"id": 692799105, "status_display": "Accepted", "lang": "golang", "question_id": 1, "title_slug": "two-sum", "code": "\nfunc twoSum(numbers []int, target int) []int {\n\tnumbers_len := len(numbers)\n\tfor index, number := range numbers {\n\t\tfor index_inner := index + 1; index_inner < numbers_len; index_inner++ {\n\t\t\tif numbers[index_inner]+number == target {\n\t\t\t\treturn []int{index, index_inner}\n\t\t\t}\n\t\t}\n\t}\n\treturn []int{}\n}\n", "title": "Two Sum", "url": "/submissions/detail/692799105/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651642336, "status": 10, "runtime": "62 ms", "is_pending": "Not Pending", "memory": "3.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func twoSum(numbers []int, target int) []int {
	numbers_len := len(numbers)
	for index, number := range numbers {
		for index_inner := index + 1; index_inner < numbers_len; index_inner++ {
			if numbers[index_inner]+number == target {
				return []int{index, index_inner}
			}
		}
	}
	return []int{}
}
