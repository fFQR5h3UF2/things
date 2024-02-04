// Submission title: for Contains Duplicate
// Submission url  : https://leetcode.com/submissions/detail/691371448/
// Submission json : {"id": 691371448, "status_display": "Accepted", "lang": "golang", "question_id": 217, "title_slug": "contains-duplicate", "code": "\nfunc containsDuplicate(numbers []int) bool {\n\tif len(numbers) == 0 || len(numbers) == 1 {\n\t\treturn false\n\t}\n\toccured := make(map[int]bool)\n\tfor _, number := range numbers {\n\t\t_, isDuplicate := occured[number]\n\t\tif isDuplicate {\n\t\t\treturn true\n\t\t}\n\t\toccured[number] = true\n\t}\n\treturn false\n}\n", "title": "Contains Duplicate", "url": "/submissions/detail/691371448/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651465468, "status": 10, "runtime": "75 ms", "is_pending": "Not Pending", "memory": "9 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func containsDuplicate(numbers []int) bool {
	if len(numbers) == 0 || len(numbers) == 1 {
		return false
	}
	occured := make(map[int]bool)
	for _, number := range numbers {
		_, isDuplicate := occured[number]
		if isDuplicate {
			return true
		}
		occured[number] = true
	}
	return false
}
