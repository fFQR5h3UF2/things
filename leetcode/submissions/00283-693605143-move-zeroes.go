// Submission title: Move Zeroes
// Submission url  : https://leetcode.com/problems/move-zeroes/description/
// Submission url  : https://leetcode.com/submissions/detail/693605143/"
package submissions

func moveZeroes(nums []int) {
	count := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			count++
		} else {
			nums[i-count] = nums[i]
		}
	}
	for count > 0 {
		nums[len(nums)-count] = 0
		count--
	}

}
