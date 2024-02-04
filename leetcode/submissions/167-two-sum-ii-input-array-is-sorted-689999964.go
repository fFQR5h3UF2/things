// Submission for Two Sum II - Input Array Is Sorted
// Submission url: https://leetcode.com/submissions/detail/689999964/

package submissions

func twoSum(numbers []int, target int) []int {
	numbers_len := len(numbers)
	for index, number := range numbers {
		if number > target {
			return []int{}
		}
		for index_inner := index + 1; index_inner < numbers_len; index_inner++ {
			if numbers[index_inner]+number == target {
				return []int{index + 1, index_inner + 1}
			}
		}
	}
	return []int{}
}
