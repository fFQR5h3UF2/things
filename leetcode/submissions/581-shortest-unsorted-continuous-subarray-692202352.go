// Submission for Shortest Unsorted Continuous Subarray
// Submission url: https://leetcode.com/submissions/detail/692202352/

package submissions

func findUnsortedSubarray(numbers []int) int {
	length := len(numbers)
	// checking edge cases
	if length == 1 {
		return 0
	}
	result := make([]int, length)
	index_sort_start, index_sort_end, end_toggle := length, length, false
	result[0] = numbers[0]
	for index := 1; index < length; index++ {
		//fmt.Println(result, index_sort_start, "->", index_sort_end)
		current, previous := numbers[index], numbers[index-1]
		// if the current number is bigger and the previous number was sorted
		// (end_toggle is on), then, probably, the current index is the end of
		// the sorted subarray
		if current >= previous && end_toggle {
			index_sort_end = index
			end_toggle = false
		}
		// just push the current number in the result array because if it is
		// bigger
		if current >= previous {
			result[index] = current
			continue
		}
		// current < previous -> find the number bigger than the current
		//
		// the current number is smaller than the starting number of the unsorted subarray
		// (or the starting index is not set)
		// -> start index is invalid, finding new start index
		if index_sort_start == length || current < numbers[index_sort_start] {
			// insert the number in the correct place and move index_sort_start
			// to the correct place
			if index_sort_start == length {
				index_sort_start = index
			}
			index_sort_start = insert_smaller(numbers, result, current, index_sort_start, 0)
			continue
		}
		// the current number is bigger than the starting number of the unsorted
		// subarray, so it should be placed inside of it
		insert_smaller(numbers, result, current, index, index_sort_start)
		// toggle to move index_sort_end
		end_toggle = true
		// set start index (if not already set)
		if index < index_sort_start {
			index_sort_start = index - 1
		}
	}
	//fmt.Println(result, index_sort_start, "->", index_sort_end)
	// return length of the sorted subarray
	return index_sort_end - index_sort_start
}

func insert_smaller(numbers []int, result []int, target int, index_start int, index_end int) int {
	index_result := index_end
	for index := index_start; index >= index_end; index-- {
		if numbers[index] <= target {
			index_result = index + 1
		}
	}
	//fmt.Println("index for", target, "-", index_result)
	// target should be placed after index_result, so move everything after
	// it to the right and insert the current number
	copy(result[index_result+1:], result[index_result:])
	result[index_result] = target
	return index_result
}
