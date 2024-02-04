// Submission for Maximum Subarray
// Submission url: https://leetcode.com/submissions/detail/691424444/

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
	//fmt.Println("here")
	for index := 1; index < length; index++ {
		//fmt.Println("index", index)
		for indexInner := index + 1; indexInner <= length; indexInner++ {
			sum := sums[indexInner] - sums[index]
			if sum > biggestSum {
				biggestSum = sum
			}
		}
	}
	return biggestSum
}
