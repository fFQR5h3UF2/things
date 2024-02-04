// Submission title: for Build an Array With Stack Operations
// Submission url  : https://leetcode.com/submissions/detail/1090492801/
// Submission json : {"id": 1090492801, "status_display": "Accepted", "lang": "golang", "question_id": 1552, "title_slug": "build-an-array-with-stack-operations", "code": "func buildArray(target []int, n int) []string {\n    ops := []string{}\n    length := len(target)\n    matchNext, matchNextVal := 0, target[0]\n    for i := 1; i <= n; i++ {\n        if i == matchNextVal {\n            ops = append(ops, \"Push\")\n            matchNext += 1\n            if matchNext == length {\n                break\n            }\n            matchNextVal = target[matchNext]\n        } else {\n            ops = append(ops, \"Push\", \"Pop\")\n        }\n    }\n    return ops\n}", "title": "Build an Array With Stack Operations", "url": "/submissions/detail/1090492801/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699002885, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "2.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func buildArray(target []int, n int) []string {
	ops := []string{}
	length := len(target)
	matchNext, matchNextVal := 0, target[0]
	for i := 1; i <= n; i++ {
		if i == matchNextVal {
			ops = append(ops, "Push")
			matchNext += 1
			if matchNext == length {
				break
			}
			matchNextVal = target[matchNext]
		} else {
			ops = append(ops, "Push", "Pop")
		}
	}
	return ops
}
