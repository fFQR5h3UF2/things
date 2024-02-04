// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691432362/

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
	sumTemp := 0
	for index, number := range numbers {
		sumTemp += number
		sums[index] = sumTemp
		if number > biggestSum {
			biggestSum = number
		}
		if sumTemp > biggestSum {
			biggestSum = sumTemp
		}
	}
	for index := 1; index < length; index++ {
		indexToEnd := sums[length] - sums[index]
		for indexInner := index + 1; indexInner < length; indexInner++ {
			sum := indexToEnd - sums[indexInner]
			if sum > biggestSum {
				biggestSum = sum
			}
		}
	}
	return biggestSum
}
