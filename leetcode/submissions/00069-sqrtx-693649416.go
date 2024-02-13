// Submission title: Sqrt(x)
// Submission url  : https://leetcode.com/problems/sqrtx/description/
// Submission url  : https://leetcode.com/submissions/detail/693649416/
// Submission json : {"id":693649416,"status_display":"Accepted","lang":"golang","question_id":69,"title_slug":"sqrtx","code":"\nfunc mySqrt(number int) int {\n\tleft, right := 0, number\n\tfor right >= left {\n\t\tcurrent := left + (right-left)/2\n\t\tsquare_current := current * current\n\t\tsquare_next := (current + 1) * (current + 1)\n\t\tswitch {\n\t\tcase square_current <= number && square_next > number:\n\t\t\t// found the target\n\t\t\treturn current\n\t\tcase square_current > number:\n\t\t\t// target is to the left -> discard right\n\t\t\tright = current - 1\n\t\tcase square_current < number:\n\t\t\t// target is to the right -> discard left\n\t\t\tleft = current + 1\n\t\t}\n\t}\n\treturn -1\n}","title":"Sqrt(x)","url":"/submissions/detail/693649416/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651754230,"status":10,"runtime":"2 ms","is_pending":"Not Pending","memory":"2 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func mySqrt(number int) int {
	left, right := 0, number
	for right >= left {
		current := left + (right-left)/2
		square_current := current * current
		square_next := (current + 1) * (current + 1)
		switch {
		case square_current <= number && square_next > number:
			// found the target
			return current
		case square_current > number:
			// target is to the left -> discard right
			right = current - 1
		case square_current < number:
			// target is to the right -> discard left
			left = current + 1
		}
	}
	return -1
}
