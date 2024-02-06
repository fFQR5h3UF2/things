// Submission title: for Merge Strings Alternately
// Submission url  : https://leetcode.com/submissions/detail/1093844607/
// Submission json : {"id": 1093844607, "status_display": "Accepted", "lang": "golang", "question_id": 1894, "title_slug": "merge-strings-alternately", "code": "func mergeAlternately(word1 string, word2 string) string {\n    var sb strings.Builder\n    length1, length2 := len(word1), len(word2)\n    for i := 0; i < max(length1, length2); i++ {\n        if i == length1 {\n            sb.WriteString(word2[i:length2])\n            break\n        }\n        if i == length2 {\n            sb.WriteString(word1[i:length1])\n            break\n        }\n        sb.WriteByte(word1[i])\n        sb.WriteByte(word2[i])\n    }\n    return sb.String()\n}", "title": "Merge Strings Alternately", "url": "/submissions/detail/1093844607/", "lang_name": "Go", "time": "2\u00a0months, 4\u00a0weeks", "timestamp": 1699383048, "status": 10, "runtime": "1 ms", "is_pending": "Not Pending", "memory": "2.1 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func mergeAlternately(word1 string, word2 string) string {
	var sb strings.Builder
	length1, length2 := len(word1), len(word2)
	for i := 0; i < max(length1, length2); i++ {
		if i == length1 {
			sb.WriteString(word2[i:length2])
			break
		}
		if i == length2 {
			sb.WriteString(word1[i:length1])
			break
		}
		sb.WriteByte(word1[i])
		sb.WriteByte(word2[i])
	}
	return sb.String()
}
