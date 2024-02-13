// Submission title: Guess Number Higher or Lower
// Submission url  : https://leetcode.com/problems/guess-number-higher-or-lower/description/
// Submission url  : https://leetcode.com/submissions/detail/691650979/
// Submission json : {"id":691650979,"status_display":"Accepted","lang":"golang","question_id":374,"title_slug":"guess-number-higher-or-lower","code":"\nfunc guessNumber(n int) int {\n\t// checking edge cases\n\tif guess(1) == 0 {\n\t\treturn 1\n\t} else if guess(n) == 0 {\n\t\treturn n\n\t}\n\tleft, right := 1, n\n\tfor right >= left {\n\t\t// overflow protection\n\t\tnumber := left + (right-left)/2\n\t\tswitch guess(number) {\n\t\tcase 0:\n\t\t\t// found the target\n\t\t\treturn number\n\t\tcase -1:\n\t\t\t// the number is bigger -> the target is to the left -> discard right\n\t\t\tright = number - 1\n\t\tcase 1:\n\t\t\t// the number is smaller -> the target is to the right -> discard left\n\t\t\tleft = number + 1\n\t\t}\n\t}\n\t// ide shows an error, this return is unreachable in this issue\n\treturn 0\n}\n","title":"Guess Number Higher or Lower","url":"/submissions/detail/691650979/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651502962,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"1.9 MB","compare_result":"1111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func guessNumber(n int) int {
	// checking edge cases
	if guess(1) == 0 {
		return 1
	} else if guess(n) == 0 {
		return n
	}
	left, right := 1, n
	for right >= left {
		// overflow protection
		number := left + (right-left)/2
		switch guess(number) {
		case 0:
			// found the target
			return number
		case -1:
			// the number is bigger -> the target is to the left -> discard right
			right = number - 1
		case 1:
			// the number is smaller -> the target is to the right -> discard left
			left = number + 1
		}
	}
	// ide shows an error, this return is unreachable in this issue
	return 0
}
