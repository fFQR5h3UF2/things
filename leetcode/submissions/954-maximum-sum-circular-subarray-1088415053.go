// Submission for Maximum Sum Circular Subarray
// Submission url: https://leetcode.com/submissions/detail/1088415053/

package submissions

func maxSubarraySumCircular(nums []int) int {
    length := len(nums)
    var maxSumOverall *int

    for i := 0; i < length; i++ {
        sum, maxSum := nums[i], nums[i]
        for j := 1; j < length; j++ {
            sum += nums[(i + j) % length]
            if sum > maxSum {
                maxSum = sum
            }
        }
        if maxSumOverall == nil {
            maxSumOverall = &maxSum
        } else if maxSum > *maxSumOverall {
            *maxSumOverall = maxSum
        }
    }
    return *maxSumOverall
}
