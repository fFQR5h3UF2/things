// Submission for Two Sum
// Submission url: https://leetcode.com/submissions/detail/689993907/

package submissions

func twoSum(numbers []int, target int) []int {
	numbers_len := len(numbers)
	for index, number := range numbers {
		if number == target {
			return []int{index}
		}
		sum := number
		for index_inner := index + 1; index_inner < numbers_len; index_inner++ {
			sum += numbers[index_inner]
			if sum == target {
				return []int{index, index_inner}
			}
		}
	}
	return []int{}
}
