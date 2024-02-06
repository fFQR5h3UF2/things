// Submission title: for Maximum Sum Circular Subarray
// Submission url  : https://leetcode.com/submissions/detail/1088426545/
// Submission json : {"id": 1088426545, "status_display": "Accepted", "lang": "golang", "question_id": 954, "title_slug": "maximum-sum-circular-subarray", "code": "func max(a, b int) int {\n    if a > b {\n        return a\n    }\n    return b\n}\n\nfunc min(a, b int) int {\n    if a < b {\n        return a\n    }\n    return b\n}\n\nfunc maxSubarraySumCircular(nums []int) int {\n    var max_sum_ending_here int = 0\n    var min_sum_ending_here int = 0\n    var max_sum_so_far int = math.MinInt\n    var min_sum_so_far int = math.MaxInt\n    var total = 0\n    for i := 0; i < len(nums); i++ {\n        total += nums[i]\n        max_sum_ending_here += nums[i]\n        min_sum_ending_here += nums[i]\n        max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)\n        min_sum_so_far = min(min_sum_so_far, min_sum_ending_here)\n        max_sum_ending_here = max(max_sum_ending_here, 0)\n        min_sum_ending_here = min(min_sum_ending_here, 0)\n    }\n    if max_sum_so_far < 0 {\n        return max_sum_so_far\n    }\n    return max(max_sum_so_far, total - min_sum_so_far)\n}", "title": "Maximum Sum Circular Subarray", "url": "/submissions/detail/1088426545/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698765236, "status": 10, "runtime": "47 ms", "is_pending": "Not Pending", "memory": "6.9 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxSubarraySumCircular(nums []int) int {
	var max_sum_ending_here int = 0
	var min_sum_ending_here int = 0
	var max_sum_so_far int = math.MinInt
	var min_sum_so_far int = math.MaxInt
	var total = 0
	for i := 0; i < len(nums); i++ {
		total += nums[i]
		max_sum_ending_here += nums[i]
		min_sum_ending_here += nums[i]
		max_sum_so_far = max(max_sum_so_far, max_sum_ending_here)
		min_sum_so_far = min(min_sum_so_far, min_sum_ending_here)
		max_sum_ending_here = max(max_sum_ending_here, 0)
		min_sum_ending_here = min(min_sum_ending_here, 0)
	}
	if max_sum_so_far < 0 {
		return max_sum_so_far
	}
	return max(max_sum_so_far, total-min_sum_so_far)
}
