// Submission title: Build an Array With Stack Operations
// Submission url  : https://leetcode.com/problems/build-an-array-with-stack-operations/description/
// Submission url  : https://leetcode.com/submissions/detail/1090492007/
// Submission json : {"id":1090492007,"status_display":"Accepted","lang":"golang","question_id":1552,"title_slug":"build-an-array-with-stack-operations","code":"func buildArray(target []int, n int) []string {\n    ops := []string{}\n    length := len(target)\n    matchNext := 0\n    for i := 1; i <= n; i++ {\n        if matchNext == length {\n            break\n        }\n        ops = append(ops, \"Push\")\n        if i == target[matchNext] {\n            matchNext += 1\n        } else {\n            ops = append(ops, \"Pop\")\n        }\n    }\n    return ops\n}","title":"Build an Array With Stack Operations","url":"/submissions/detail/1090492007/","lang_name":"Go","time":"3 months","timestamp":1699002784,"status":10,"runtime":"2 ms","is_pending":"Not Pending","memory":"2.4 MB","compare_result":"1111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func buildArray(target []int, n int) []string {
	ops := []string{}
	length := len(target)
	matchNext := 0
	for i := 1; i <= n; i++ {
		if matchNext == length {
			break
		}
		ops = append(ops, "Push")
		if i == target[matchNext] {
			matchNext += 1
		} else {
			ops = append(ops, "Pop")
		}
	}
	return ops
}
