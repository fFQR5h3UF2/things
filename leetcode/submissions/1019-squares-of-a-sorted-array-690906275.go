// Submission for Squares of a Sorted Array
// Submission url: https://leetcode.com/submissions/detail/690906275/

package submissions

func sortedSquares(numbers []int) []int {
	length := len(numbers)
	if length == 0 || length == 1 {
		return square(numbers)
	}
	negativesIndex := 0
	for index, number := range numbers {
		if number >= 0 {
			negativesIndex = index
			break
		}
	}
	if negativesIndex == length-1 || negativesIndex == 0 {
		return square(numbers)
	}
	//fmt.Println("negativesIndex", negativesIndex)
	result, resultIndex, negativesIndex := make([]int, length), 0, negativesIndex-1
	for positivesIndex := negativesIndex + 1; positivesIndex < length; positivesIndex++ {
		for ; negativesIndex >= 0 && numbers[negativesIndex]*-1 <= numbers[positivesIndex]; negativesIndex-- {
			result[resultIndex] = numbers[negativesIndex]
			resultIndex++
			//fmt.Println("negative", negativesIndex, numbers[negativesIndex], result, numbers)
		}
		//fmt.Println("positivesIndex", positivesIndex, numbers[positivesIndex], result, numbers)
		result[resultIndex] = numbers[positivesIndex]
		resultIndex++
	}
	return square(result)
}

func square(array []int) []int {
	for index, number := range array {
		array[index] = number * number
	}
	return array
}
