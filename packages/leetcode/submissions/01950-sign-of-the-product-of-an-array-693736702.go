// Submission title: for Sign of the Product of an Array
// Submission url  : https://leetcode.com/submissions/detail/693736702/
// Submission json : {"id": 693736702, "status_display": "Accepted", "lang": "golang", "question_id": 1950, "title_slug": "sign-of-the-product-of-an-array", "code": "\nfunc arraySign(numbers []int) int {\n\tnegative_count := 0\n\tfor _, number := range numbers {\n\t\tswitch {\n\t\t// the number is 0 -> product of all numbers is definitely zero\n\t\tcase number == 0:\n\t\t\treturn 0\n\t\t\t// the number is negative -> add to count\n\t\tcase number < 0:\n\t\t\tnegative_count++\n\t\t}\n\t}\n\t// even amount of negative numbers -> result is positive\n\tif negative_count&1 == 0 {\n\t\treturn 1\n\t}\n\t// uneven amount of negative numbers -> result is negative\n\treturn -1\n}", "title": "Sign of the Product of an Array", "url": "/submissions/detail/693736702/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651765192, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "3.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func arraySign(numbers []int) int {
	negative_count := 0
	for _, number := range numbers {
		switch {
		// the number is 0 -> product of all numbers is definitely zero
		case number == 0:
			return 0
			// the number is negative -> add to count
		case number < 0:
			negative_count++
		}
	}
	// even amount of negative numbers -> result is positive
	if negative_count&1 == 0 {
		return 1
	}
	// uneven amount of negative numbers -> result is negative
	return -1
}
