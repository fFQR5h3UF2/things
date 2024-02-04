// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691512168/

package submissions

func maxSubArray(numbers []int) int {
	length := len(numbers)
	switch length {
	case 0:
		return 0
	case 1:
		return numbers[0]
	}
	sums, biggestSum, biggestSumIndex := make([]int, length), numbers[0], 0
	sumFromZero := 0
	// [-2,1,-3,4,-1,2,1,-5,4]
	for index, number := range numbers {
		sumFromZero += number
		sums[index] = sumFromZero
		for indexInner := biggestSumIndex; indexInner <= index; indexInner++ {
			sum := sumFromZero
			if indexInner != 0 {
				sum -= sums[indexInner-1]
			}
			if sum > biggestSum {
				biggestSum = sum
				biggestSumIndex = indexInner
			}
		}
	}
	return biggestSum
}
