// Submission title: for Find Smallest Letter Greater Than Target
// Submission url  : https://leetcode.com/submissions/detail/693729962/
// Submission json : {"id": 693729962, "status_display": "Accepted", "lang": "golang", "question_id": 745, "title_slug": "find-smallest-letter-greater-than-target", "code": "\n\nfunc nextGreatestLetter(letters []byte, target byte) byte {\n\tlength := len(letters)\n\tleft, right := 0, length-1\n\tfor right >= left {\n\t\tindex := left + (right-left)/2\n\t\tcharacter := letters[index]\n\t\t// the character is bigger, we found at least one result\n\t\t// smaller characters are to the left -> discard right\n\t\tif character > target {\n\t\t\tright = index - 1\n\t\t\tcontinue\n\t\t}\n\t\t// character is either equal or smaller -> there is no results to the\n\t\t// left -> discard left\n\t\tleft = index + 1\n\t}\n\treturn letters[left%length]\n}\n", "title": "Find Smallest Letter Greater Than Target", "url": "/submissions/detail/693729962/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651764399, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "2.7 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func nextGreatestLetter(letters []byte, target byte) byte {
	length := len(letters)
	left, right := 0, length-1
	for right >= left {
		index := left + (right-left)/2
		character := letters[index]
		// the character is bigger, we found at least one result
		// smaller characters are to the left -> discard right
		if character > target {
			right = index - 1
			continue
		}
		// character is either equal or smaller -> there is no results to the
		// left -> discard left
		left = index + 1
	}
	return letters[left%length]
}
