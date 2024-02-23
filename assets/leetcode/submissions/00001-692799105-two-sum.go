// Submission title: Two Sum
// Submission url  : https://leetcode.com/problems/two-sum/description/
// Submission url  : https://leetcode.com/submissions/detail/692799105/"
package submissions

func twoSum(numbers []int, target int) []int {
	numbers_len := len(numbers)
	for index, number := range numbers {
		for index_inner := index + 1; index_inner < numbers_len; index_inner++ {
			if numbers[index_inner]+number == target {
				return []int{index, index_inner}
			}
		}
	}
	return []int{}
}
