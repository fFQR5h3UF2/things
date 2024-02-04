// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691570124/

package submissions



func maxSubArray(numbers []int) (result int) {
	length := len(numbers)
	switch length {
	case 0:
		return 0
	case 1:
		return numbers[0]
	}
	currentMaximum, result := numbers[0], numbers[0]
	for index := 1; index < length; index++ {
		currentMaximum += numbers[index]
		if result < currentMaximum {
			result = currentMaximum
		}
		if currentMaximum < 0 {
			currentMaximum = 0
		}
	}
	return
}
