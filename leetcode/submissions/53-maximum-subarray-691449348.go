// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691449348/

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
	sumZeroToLast := 0
	for index, number := range numbers {
		sumZeroToLast += number
		sums[index] = sumZeroToLast
		if number > biggestSum {
			biggestSum = number
		}
		if sumZeroToLast > biggestSum {
			biggestSum = sumZeroToLast
		}
	}
	// [-2,1,-3,4,-1,2,1,-5,4]
	for index := 1; index < length; index++ {
		indexToEnd := sumZeroToLast - sums[index-1]
		for indexInner := index + 1; indexInner < length; indexInner++ {
			sum := indexToEnd - (sumZeroToLast - sums[indexInner-1])
			if sum > biggestSum {
				biggestSum = sum
			}
		}
	}
	return biggestSum
}
