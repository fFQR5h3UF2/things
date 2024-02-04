// Submission title: for Maximum Subarray
// Submission url  : https://leetcode.com/submissions/detail/691571728/
// Submission json : {"id": 691571728, "status_display": "Accepted", "lang": "golang", "question_id": 53, "title_slug": "maximum-subarray", "code": "\nfunc maxSubArray(numbers []int) int {\n\tlength := len(numbers)\n\tswitch length {\n\tcase 0:\n\t\treturn 0\n\tcase 1:\n\t\treturn numbers[0]\n\t}\n\tmaxCurrent, maxOverall := 0, math.MinInt\n\tfor _, number := range numbers {\n\t\tmaxCurrent += number\n\t\tif maxCurrent > maxOverall {\n\t\t\tmaxOverall = maxCurrent\n\t\t}\n\t\tif maxCurrent < 0 {\n\t\t\tmaxCurrent = 0\n\t\t}\n\t}\n\treturn maxOverall\n}", "title": "Maximum Subarray", "url": "/submissions/detail/691571728/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651492725, "status": 10, "runtime": "123 ms", "is_pending": "Not Pending", "memory": "9.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func maxSubArray(numbers []int) int {
	length := len(numbers)
	switch length {
	case 0:
		return 0
	case 1:
		return numbers[0]
	}
	maxCurrent, maxOverall := 0, math.MinInt
	for _, number := range numbers {
		maxCurrent += number
		if maxCurrent > maxOverall {
			maxOverall = maxCurrent
		}
		if maxCurrent < 0 {
			maxCurrent = 0
		}
	}
	return maxOverall
}
