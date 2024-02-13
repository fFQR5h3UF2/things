// Submission title: Shortest Unsorted Continuous Subarray
// Submission url  : https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
// Submission url  : https://leetcode.com/submissions/detail/692226609/
// Submission json : {"id":692226609,"status_display":"Accepted","lang":"golang","question_id":581,"title_slug":"shortest-unsorted-continuous-subarray","code":"\nfunc findUnsortedSubarray(numbers []int) int {\n\tlength := len(numbers)\n\t// checking edge cases\n\tif length == 1 {\n\t\treturn 0\n\t}\n\tresult := make([]int, length)\n\t// initializing to MaxInt because zeros will impact future sorting\n\tfor index := range result {\n\t\tresult[index] = math.MaxInt\n\t}\n\tindex_sort_start, index_sort_end := length, length\n\tresult[0] = numbers[0]\n\tfor index := 1; index < length; index++ {\n//\t\tfmt.Println(result, index_sort_start, \"->\", index_sort_end)\n\t\t// current is not sorted -> from numbers\n\t\t// previous is sorted -> from result\n\t\tcurrent, previous := numbers[index], result[index-1]\n\t\t// just push the current number in the result array because if it is\n\t\t// bigger\n\t\tif current >= previous {\n\t\t\tresult[index] = current\n\t\t\tcontinue\n\t\t}\n\t\t// current number is not sorted -> moving the end index\n\t\tindex_sort_end = index + 1\n\t\t// current < previous -> find the number bigger than the current\n\t\t//\n\t\t// the current number is smaller than the starting number of the unsorted subarray\n\t\t// (or the starting index is not set)\n\t\t// -> start index is invalid, finding new start index in numbers\n\t\tif index_sort_start == length || current < result[index_sort_start] {\n\t\t\t// insert the number in the correct place and move index_sort_start\n\t\t\t// to the correct place\n\t\t\tif index_sort_start == length {\n\t\t\t\t// index_sort_start is not set -> setting to the last sorted number\n\t\t\t\tindex_sort_start = index - 1\n\t\t\t}\n\t\t\tindex_sort_start = insert_smaller(result, current, index_sort_start, 0)\n\t\t\tcontinue\n\t\t}\n\t\t// the current number is bigger than the starting number of the unsorted\n\t\t// subarray, so it should be placed inside of it\n\t\tinsert_smaller(result, current, index, index_sort_start)\n\t\t// set start index (if not already set)\n\t\tif index < index_sort_start {\n\t\t\tindex_sort_start = index - 1\n\t\t}\n\t}\n//\tfmt.Println(result, index_sort_start, \"->\", index_sort_end)\n\t// return length of the sorted subarray\n\treturn index_sort_end - index_sort_start\n}\n\nfunc insert_smaller(numbers []int, target int, index_start int, index_end int) int {\n\tindex_result := index_end\n\tfor index := index_start; index >= index_end; index-- {\n\t\tif target >= numbers[index] {\n\t\t\t// target is bigger -> it should be placed after this index\n\t\t\tindex_result = index + 1\n\t\t\tbreak\n\t\t}\n\t}\n//\tfmt.Println(\"index for\", target, \"-\", index_result)\n\t// target should be placed after index_result, so move everything after\n\t// it to the right and insert the current number\n\t// if index_result is the last item, then just push it\n\tcopy(numbers[index_result+1:], numbers[index_result:])\n\tnumbers[index_result] = target\n\treturn index_result\n}\n","title":"Shortest Unsorted Continuous Subarray","url":"/submissions/detail/692226609/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651573060,"status":10,"runtime":"152 ms","is_pending":"Not Pending","memory":"6.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func findUnsortedSubarray(numbers []int) int {
	length := len(numbers)
	// checking edge cases
	if length == 1 {
		return 0
	}
	result := make([]int, length)
	// initializing to MaxInt because zeros will impact future sorting
	for index := range result {
		result[index] = math.MaxInt
	}
	index_sort_start, index_sort_end := length, length
	result[0] = numbers[0]
	for index := 1; index < length; index++ {
		//		fmt.Println(result, index_sort_start, "->", index_sort_end)
		// current is not sorted -> from numbers
		// previous is sorted -> from result
		current, previous := numbers[index], result[index-1]
		// just push the current number in the result array because if it is
		// bigger
		if current >= previous {
			result[index] = current
			continue
		}
		// current number is not sorted -> moving the end index
		index_sort_end = index + 1
		// current < previous -> find the number bigger than the current
		//
		// the current number is smaller than the starting number of the unsorted subarray
		// (or the starting index is not set)
		// -> start index is invalid, finding new start index in numbers
		if index_sort_start == length || current < result[index_sort_start] {
			// insert the number in the correct place and move index_sort_start
			// to the correct place
			if index_sort_start == length {
				// index_sort_start is not set -> setting to the last sorted number
				index_sort_start = index - 1
			}
			index_sort_start = insert_smaller(result, current, index_sort_start, 0)
			continue
		}
		// the current number is bigger than the starting number of the unsorted
		// subarray, so it should be placed inside of it
		insert_smaller(result, current, index, index_sort_start)
		// set start index (if not already set)
		if index < index_sort_start {
			index_sort_start = index - 1
		}
	}
	//	fmt.Println(result, index_sort_start, "->", index_sort_end)
	// return length of the sorted subarray
	return index_sort_end - index_sort_start
}

func insert_smaller(numbers []int, target int, index_start int, index_end int) int {
	index_result := index_end
	for index := index_start; index >= index_end; index-- {
		if target >= numbers[index] {
			// target is bigger -> it should be placed after this index
			index_result = index + 1
			break
		}
	}
	//	fmt.Println("index for", target, "-", index_result)
	// target should be placed after index_result, so move everything after
	// it to the right and insert the current number
	// if index_result is the last item, then just push it
	copy(numbers[index_result+1:], numbers[index_result:])
	numbers[index_result] = target
	return index_result
}
