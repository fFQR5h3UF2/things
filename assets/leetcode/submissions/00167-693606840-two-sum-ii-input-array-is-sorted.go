// Submission title: Two Sum II - Input Array Is Sorted
// Submission url  : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
// Submission url  : https://leetcode.com/submissions/detail/693606840/"
package submissions

func twoSum(numbers []int, target int) []int {
	numbers_len := len(numbers)
	for index, number := range numbers {
		for index_inner := index + 1; index_inner < numbers_len; index_inner++ {
			if numbers[index_inner]+number == target {
				return []int{index + 1, index_inner + 1}
			}
		}
	}
	return []int{}
}
