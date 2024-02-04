// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691501267/

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
	// [-2,1,-3,4,-1,2,1,-5,4]
	for index := 0; index < length; index++ {
		for indexInner := biggestSumIndex; indexInner >= biggestSumIndex && indexInner <= index; indexInner++ {
			sums[indexInner] += numbers[index]
			if sums[indexInner] > biggestSum {
				biggestSum = sums[indexInner]
				biggestSumIndex = indexInner
			}
		}
	}
	return biggestSum
}
