// Submission title: Squares of a Sorted Array
// Submission url  : https://leetcode.com/problems/squares-of-a-sorted-array/description/
// Submission url  : https://leetcode.com/submissions/detail/1191505117/"
package submissions

func sortedSquares(nums []int) []int {
	for i, num := range nums {
		if num < 0 {
			nums[i] = -num
		}
	}
	slices.Sort(nums)
	for i, num := range nums {
		nums[i] = num * num
	}
	return nums
}
