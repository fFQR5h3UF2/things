// Submission title: for Count Number of Homogenous Substrings
// Submission url  : https://leetcode.com/submissions/detail/1095037372/
// Submission json : {"id": 1095037372, "status_display": "Accepted", "lang": "golang", "question_id": 1885, "title_slug": "count-number-of-homogenous-substrings", "code": "func countHomogenous(s string) int {\n    var (\n        mod int64 = 1000000007 \n        total int64 = 0\n        count int64 = 0\n        cur = s[0]\n    )\n    \n    for i := 0; i < len(s); i++ {\n        char := s[i]\n        if char == cur {\n            count++\n        } else {\n            count = 1\n            cur = char\n        }\n        total += count\n    }\n    \n    return int(total % mod)\n}", "title": "Count Number of Homogenous Substrings", "url": "/submissions/detail/1095037372/", "lang_name": "Go", "time": "2\u00a0months, 3\u00a0weeks", "timestamp": 1699513420, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "6.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func countHomogenous(s string) int {
	var (
		mod   int64 = 1000000007
		total int64 = 0
		count int64 = 0
		cur         = s[0]
	)

	for i := 0; i < len(s); i++ {
		char := s[i]
		if char == cur {
			count++
		} else {
			count = 1
			cur = char
		}
		total += count
	}

	return int(total % mod)
}
