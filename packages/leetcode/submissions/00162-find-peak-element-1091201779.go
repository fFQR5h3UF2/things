// Submission title: for Find Peak Element
// Submission url  : https://leetcode.com/submissions/detail/1091201779/
// Submission json : {"id": 1091201779, "status_display": "Accepted", "lang": "golang", "question_id": 162, "title_slug": "find-peak-element", "code": "func findPeakElement(nums []int) int {\n    left := 0\n    right := len(nums) - 1\n    \n    for left < right {\n        mid := left + (right - left) / 2\n        \n        if nums[mid] > nums[mid+1] {\n            // The peak is in the left half\n            right = mid\n        } else {\n            // The peak is in the right half\n            left = mid + 1\n        }\n    }\n    \n    return left\n}", "title": "Find Peak Element", "url": "/submissions/detail/1091201779/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093827, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "2.7 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func findPeakElement(nums []int) int {
	left := 0
	right := len(nums) - 1

	for left < right {
		mid := left + (right-left)/2

		if nums[mid] > nums[mid+1] {
			// The peak is in the left half
			right = mid
		} else {
			// The peak is in the right half
			left = mid + 1
		}
	}

	return left
}
