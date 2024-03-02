// Submission title: Squares of a Sorted Array
// Submission url  : https://leetcode.com/problems/squares-of-a-sorted-array/description/
// Submission url  : https://leetcode.com/submissions/detail/1191505496/"
package submissions

func sortedSquares(nums []int) []int {
	for i, num := range nums {
		nums[i] = num * num
	}
	slices.Sort(nums)
	return nums
}
