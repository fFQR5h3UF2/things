// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691485056/

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
	checked := make([]int, length)
	for index := 0; index < length; index++ {
		number := numbers[index]
		sumZeroToCurrent += number
		sums[index] = sumZeroToCurrent
		switch {
		case number > biggestSum:
			biggestSum = number
		case sumZeroToCurrent > biggestSum:
			biggestSum = sumZeroToCurrent
		}
		checked[index] = 0
		for indexInner := 1; indexInner <= index; indexInner++ {
			if indexInner < checked[indexInner] {
				continue
			}
			sum := sumZeroToCurrent - sums[indexInner-1]
			if sum > biggestSum {
				biggestSum = sum
			}
		}
		checked[index] = index
	}
	return biggestSum
}
