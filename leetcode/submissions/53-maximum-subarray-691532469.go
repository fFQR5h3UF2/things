// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691532469/

package submissions


func maxSubArray(numbers []int) int {
	length := len(numbers)
	switch length {
	case 0:
		return 0
	case 1:
		return numbers[0]
	}
	sums, biggestSumIndex := make([]int, length), 0
	// [-2,1,-3,4,-1,2,1,-5,4]
	for index := 0; index < length; index++ {
		number := numbers[index]
		sums[biggestSumIndex] += number
		sums[index] = sums[biggestSumIndex]
		//fmt.Println(index, biggestSumIndex)
		switch {
		case number >= sums[biggestSumIndex]:
			// no need to check subarrays if the new number is bigger than the sum
			sums[biggestSumIndex], biggestSumIndex = number, index
			fallthrough
		case index != 0 && number >= numbers[index-1]:
			// no need to check subarrays if the new number is bigger than the previous
			continue
		}
		for indexInner := biggestSumIndex + 1; indexInner < index; indexInner++ {
			sum := sums[biggestSumIndex]
			if indexInner != 0 {
				sum -= sums[indexInner-1]
			}
			if sum > sums[biggestSumIndex] {
				sums[biggestSumIndex], biggestSumIndex = sum, indexInner
			}
			//fmt.Println("inner", indexInner, biggestSumIndex)
		}
	}
	return sums[biggestSumIndex]
}
