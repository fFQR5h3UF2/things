// Submission title: for Squares of a Sorted Array
// Submission url  : https://leetcode.com/submissions/detail/690922740/
// Submission json : {"id": 690922740, "status_display": "Accepted", "lang": "golang", "question_id": 1019, "title_slug": "squares-of-a-sorted-array", "code": "\nfunc sortedSquares(numbers []int) []int {\n\tlength := len(numbers)\n\tif length == 0 || length == 1 {\n\t\treturn square(numbers, false)\n\t}\n\tnegativesIndex := -1\n\tfor index, number := range numbers {\n\t\tif number >= 0 {\n\t\t\tnegativesIndex = index\n\t\t\tbreak\n\t\t}\n\t}\n\tif negativesIndex == 0 || negativesIndex == -1 {\n\t\treturn square(numbers, negativesIndex == -1)\n\t}\n\t//fmt.Println(\"negativesIndex\", negativesIndex)\n\tresult, resultIndex, negativesIndex := make([]int, length), 0, negativesIndex-1\n\tfor positivesIndex := negativesIndex + 1; resultIndex < length; positivesIndex++ {\n\t\tpositiveOverflow := positivesIndex >= length\n\t\tfor {\n\t\t\tif negativesIndex < 0 || resultIndex >= length {\n\t\t\t\tbreak\n\t\t\t}\n\t\t\tif !positiveOverflow && numbers[negativesIndex]*-1 > numbers[positivesIndex] {\n\t\t\t\tbreak\n\t\t\t}\n\t\t\t\n\t\t\tresult[resultIndex] = numbers[negativesIndex]\n\t\t\tresultIndex++\n\t\t\t//fmt.Println(\"negative\", negativesIndex, resultIndex, numbers[negativesIndex], result, numbers)\n            negativesIndex--\n\t\t}\n\t\tif resultIndex < length && !positiveOverflow {\n\t//\t\tfmt.Println(\"positivesIndex\", positivesIndex, resultIndex, numbers[positivesIndex], result, numbers)\n\t\t\tresult[resultIndex] = numbers[positivesIndex]\n\t\t\tresultIndex++\n\t\t}\n\t}\n\treturn square(result, false)\n}\n\nfunc square(array []int, reverse bool) []int {\n\tif reverse {\n\t\tlength := len(array)\n\t\treversed := make([]int, length)\n\t\tfor index := length - 1; index >= 0; index-- {\n\t\t\treversed[length-index-1] = array[index] * array[index]\n\t\t}\n\t\treturn reversed\n\t} else {\n\t\tfor index, number := range array {\n\t\t\tarray[index] = number * number\n\t\t}\n\t\treturn array\n\t}\n}\n", "title": "Squares of a Sorted Array", "url": "/submissions/detail/690922740/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651408868, "status": 10, "runtime": "27 ms", "is_pending": "Not Pending", "memory": "7 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func sortedSquares(numbers []int) []int {
	length := len(numbers)
	if length == 0 || length == 1 {
		return square(numbers, false)
	}
	negativesIndex := -1
	for index, number := range numbers {
		if number >= 0 {
			negativesIndex = index
			break
		}
	}
	if negativesIndex == 0 || negativesIndex == -1 {
		return square(numbers, negativesIndex == -1)
	}
	//fmt.Println("negativesIndex", negativesIndex)
	result, resultIndex, negativesIndex := make([]int, length), 0, negativesIndex-1
	for positivesIndex := negativesIndex + 1; resultIndex < length; positivesIndex++ {
		positiveOverflow := positivesIndex >= length
		for {
			if negativesIndex < 0 || resultIndex >= length {
				break
			}
			if !positiveOverflow && numbers[negativesIndex]*-1 > numbers[positivesIndex] {
				break
			}

			result[resultIndex] = numbers[negativesIndex]
			resultIndex++
			//fmt.Println("negative", negativesIndex, resultIndex, numbers[negativesIndex], result, numbers)
			negativesIndex--
		}
		if resultIndex < length && !positiveOverflow {
			//		fmt.Println("positivesIndex", positivesIndex, resultIndex, numbers[positivesIndex], result, numbers)
			result[resultIndex] = numbers[positivesIndex]
			resultIndex++
		}
	}
	return square(result, false)
}

func square(array []int, reverse bool) []int {
	if reverse {
		length := len(array)
		reversed := make([]int, length)
		for index := length - 1; index >= 0; index-- {
			reversed[length-index-1] = array[index] * array[index]
		}
		return reversed
	} else {
		for index, number := range array {
			array[index] = number * number
		}
		return array
	}
}
