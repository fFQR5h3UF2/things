// Submission title: for Subtract the Product and Sum of Digits of an Integer
// Submission url  : https://leetcode.com/submissions/detail/692713623/
// Submission json : {"id": 692713623, "status_display": "Accepted", "lang": "golang", "question_id": 1406, "title_slug": "subtract-the-product-and-sum-of-digits-of-an-integer", "code": "func subtractProductAndSum(number int) int {\n\tfist_digit := number % 10\n\tfactorial, sum := fist_digit, fist_digit\n\tnumber /= 10\n\tfor number > 0 {\n\t\tdigit := number % 10\n\t\tfactorial *= digit\n\t\tsum += digit\n\t\tnumber /= 10\n\t}\n\treturn factorial - sum\n}\n", "title": "Subtract the Product and Sum of Digits of an Integer", "url": "/submissions/detail/692713623/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651633074, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "1.9 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func subtractProductAndSum(number int) int {
	fist_digit := number % 10
	factorial, sum := fist_digit, fist_digit
	number /= 10
	for number > 0 {
		digit := number % 10
		factorial *= digit
		sum += digit
		number /= 10
	}
	return factorial - sum
}
