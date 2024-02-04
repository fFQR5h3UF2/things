// Submission for Sqrt(x)
// Submission url: https://leetcode.com/submissions/detail/693642213/

package submissions


func mySqrt(number int) int {
	left, right := 0, number
	current := 0
	for right >= left {
		current = left + (right-left)/2
		square := current * current
		switch {
		case square == number:
			// found the target
			return current
		case square > number:
			// target is to the left -> discard right
			right = current - 1
		case square < number:
			// target is to the right -> discard left
			left = current + 1
		}
	}
	return current - 1
}
