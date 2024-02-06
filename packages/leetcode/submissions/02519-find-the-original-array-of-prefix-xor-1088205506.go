// Submission title: for Find The Original Array of Prefix Xor
// Submission url  : https://leetcode.com/submissions/detail/1088205506/
// Submission json : {"id": 1088205506, "status_display": "Accepted", "lang": "golang", "question_id": 2519, "title_slug": "find-the-original-array-of-prefix-xor", "code": "func findArray(pref []int) []int {\n    prev := pref[0]\n    for i := 1; i < len(pref); i++ {\n        cur := pref[i]\n        prev, pref[i] = cur, prev ^ cur \n    }\n    return pref\n}", "title": "Find The Original Array of Prefix Xor", "url": "/submissions/detail/1088205506/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698741218, "status": 10, "runtime": "98 ms", "is_pending": "Not Pending", "memory": "8.5 MB", "compare_result": "1111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func findArray(pref []int) []int {
	prev := pref[0]
	for i := 1; i < len(pref); i++ {
		cur := pref[i]
		prev, pref[i] = cur, prev^cur
	}
	return pref
}
