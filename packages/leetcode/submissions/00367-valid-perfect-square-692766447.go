// Submission title: for Valid Perfect Square
// Submission url  : https://leetcode.com/submissions/detail/692766447/
// Submission json : {"id": 692766447, "status_display": "Accepted", "lang": "golang", "question_id": 367, "title_slug": "valid-perfect-square", "code": "\nfunc isPerfectSquare(number int) bool {\n\tleft, right := 1, number\n\tfor right >= left {\n\t\tcurrent := left + (right-left)/2\n\t\tsquare := current * current\n\t\tswitch {\n\t\tcase square == number:\n\t\t\t// found the target\n\t\t\treturn true\n\t\tcase square > number:\n\t\t\t// square is bigger -> root is to the left -> discard right\n\t\t\tright = current - 1\n\t\tcase square < number:\n\t\t\t// square is smaller -> root is to the right -> discard left\n\t\t\tleft = current + 1\n\t\t}\n\t}\n\treturn false\n}", "title": "Valid Perfect Square", "url": "/submissions/detail/692766447/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651638864, "status": 10, "runtime": "0 ms", "is_pending": "Not Pending", "memory": "1.9 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func isPerfectSquare(number int) bool {
	left, right := 1, number
	for right >= left {
		current := left + (right-left)/2
		square := current * current
		switch {
		case square == number:
			// found the target
			return true
		case square > number:
			// square is bigger -> root is to the left -> discard right
			right = current - 1
		case square < number:
			// square is smaller -> root is to the right -> discard left
			left = current + 1
		}
	}
	return false
}
