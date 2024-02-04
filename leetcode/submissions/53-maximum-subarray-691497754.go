// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691497754/

package submissions


func maxSubArray(numbers []int) int {
	length := len(numbers)
	switch length {
	case 0:
		return 0
	case 1:
		return numbers[0]
	}
	sums, biggestSum, sumFromZero := make([]int, length), numbers[0], 0
	// [-2,1,-3,4,-1,2,1,-5,4]
	for index := 0; index < length; index++ {
		number := numbers[index]
		sumFromZero += number
		for indexInner := 0; indexInner <= index; indexInner++ {
			sums[indexInner] += number
			if sums[indexInner] > biggestSum {
				biggestSum = sums[indexInner]
			}
		}
	}
	return biggestSum
}
