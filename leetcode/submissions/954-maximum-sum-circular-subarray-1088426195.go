// Submission for Maximum Sum Circular Subarray
// Submission url: https://leetcode.com/submissions/detail/1088426195/

package submissions

func maxSubarraySumCircular(nums []int) int {
    ans := nums[0]
    n := len(nums)
    for i := 0; i < len(nums); i++ {
        currMax := nums[i]
        j := i + 1
        for j % n != i {
            currMax = max(currMax+nums[j % n], nums[j % n])
            ans = max(ans, currMax)
            j++
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
