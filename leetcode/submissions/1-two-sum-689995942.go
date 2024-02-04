// Submission for Two Sum
// Submission url: https://leetcode.com/submissions/detail/689995942/

package submissions


func find_0(numbers []int) (zeros []int) {
	for index, number := range numbers {
		if number == 0 {
			zeros = append(zeros, index)
		}
	}
	return
}

// https://leetcode.com/problems/two-sum/
func twoSum(numbers []int, target int) []int {
	numbers_len := len(numbers)
	for index, number := range numbers {
		if number == 0 {
			return find_0(numbers)
		} else if number == target {
			return []int{index}
		}
		for index_inner := index + 1; index_inner < numbers_len; index_inner++ {
			if numbers[index_inner]+number == target {
				return []int{index, index_inner}
			}
		}
	}
	return []int{}
}
