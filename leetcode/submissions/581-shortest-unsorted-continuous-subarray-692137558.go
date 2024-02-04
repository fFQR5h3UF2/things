// Submission for Shortest Unsorted Continuous Subarray
// Submission url: https://leetcode.com/submissions/detail/692137558/

package submissions


func findUnsortedSubarray(numbers []int) int {
	length := len(numbers)
	if length == 1 {
		return 0
	}
	result := make([]int, length)
	index_sort_start, index_sort_end := length, 1
	result[0] = numbers[0]
	for index := 1; index < length; index++ {
		fmt.Println(result)
		current, previous := numbers[index], numbers[index-1]
		if current >= previous {
			result[index] = current
			index_sort_end = index
			continue
		}
		result[index], result[index-1] = previous, current
		if index < index_sort_start {
			index_sort_start = index-1
		}
	}
	return index_sort_end - index_sort_start + 1
}
