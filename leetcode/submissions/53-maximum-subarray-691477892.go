// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691477892/

package submissions

func maxSubArray(numbers []int) int {
	length := len(numbers)
	switch length {
	case 0:
		return 0
	case 1:
		return numbers[0]
	}
	sums, biggestSum, sumZeroToCurrent := make([]int, length), numbers[0], 0
	for index := 0; index < length; index++ {
		number := numbers[index]
		sumZeroToCurrent += number
		sums[index] = sumZeroToCurrent
		if number > biggestSum {
			biggestSum = number
		}
		if sumZeroToCurrent > biggestSum {
			biggestSum = sumZeroToCurrent
		}
		for indexInner := 1; indexInner <= index; indexInner++ {
			sum := sumZeroToCurrent - sums[indexInner-1]
			if sum > biggestSum {
				biggestSum = sum
			}
		}
	}
	return biggestSum
}
