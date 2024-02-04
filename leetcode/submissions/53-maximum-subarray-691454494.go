// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691454494/

package submissions


func maxSubArray(numbers []int) int {
	length := len(numbers)
	switch length {
	case 0:
		return 0
	case 1:
		return numbers[0]
	}
	sums := make(map[int]int, length)
	biggestSum := numbers[0]
	sumAll := 0
	for index := length - 1; index >= 0; index-- {
		number := numbers[index]
		sumAll += number
		sums[index] = sumAll
		if number > biggestSum {
			biggestSum = number
		}
		if sumAll > biggestSum {
			biggestSum = sumAll
		}
	}
	for index := 1; index < length; index++ {
		indexToEnd := sums[index-1]
		for indexInner := index + 1; indexInner <= length; indexInner++ {
			sum := indexToEnd - sums[indexInner]
			if sum > biggestSum {
				biggestSum = sum
			}
		}
	}
	return biggestSum
}
