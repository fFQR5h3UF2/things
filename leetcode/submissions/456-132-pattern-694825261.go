// Submission for 132 Pattern
// Submission url: https://leetcode.com/submissions/detail/694825261/

package submissions


func find132pattern(numbers []int) bool {
	length := len(numbers)
	if length < 3 {
		// if the array doesn't have at least three numbers, it cannot have
		// '123' pattern
		return false
	}
	for index := 0; index+2 < length; index++ {
		first, second, third := numbers[index], numbers[index+1], numbers[index+2]
		if second > first && second > third && third > first {
			return true
		}
	}
	return false
}
