// Submission title: for Count Odd Numbers in an Interval Range
// Submission url  : https://leetcode.com/submissions/detail/691609936/
// Submission json : {"id": 691609936, "status_display": "Accepted", "lang": "golang", "question_id": 1630, "title_slug": "count-odd-numbers-in-an-interval-range", "code": "\nfunc countOdds(low int, high int) int {\n\tlow_even, high_even, half := (low&1) == 0, (high&1) == 0, (high-low)/2\n\tif low_even && high_even  {\n\t\treturn half\n\t}\n\treturn half + 1\n}", "title": "Count Odd Numbers in an Interval Range", "url": "/submissions/detail/691609936/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651498129, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "1.9 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func countOdds(low int, high int) int {
	low_even, high_even, half := (low&1) == 0, (high&1) == 0, (high-low)/2
	if low_even && high_even {
		return half
	}
	return half + 1
}
