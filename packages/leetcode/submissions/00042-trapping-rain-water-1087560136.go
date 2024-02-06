// Submission title: for Trapping Rain Water
// Submission url  : https://leetcode.com/submissions/detail/1087560136/
// Submission json : {"id": 1087560136, "status_display": "Accepted", "lang": "golang", "question_id": 42, "title_slug": "trapping-rain-water", "code": "func trap(height []int) int {\n    left, right := 0, len(height) - 1\n    res := 0\n    leftMax, rightMax := 0, 0\n\n    for left < right {\n        if height[left] < height[right] {\n            if height[left] >= leftMax {\n                leftMax = height[left]\n            } else {\n                res += (leftMax-height[left])\n            }\n            left++\n        } else {\n            if height[right] >= rightMax {\n                rightMax = height[right]\n            } else {\n                res += (rightMax-height[right])\n            }\n            right--\n        }\n    }\n\n    return res\n}", "title": "Trapping Rain Water", "url": "/submissions/detail/1087560136/", "lang_name": "Go", "time": "3\u00a0months, 1\u00a0week", "timestamp": 1698672510, "status": 10, "runtime": "6 ms", "is_pending": "Not Pending", "memory": "5.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func trap(height []int) int {
	left, right := 0, len(height)-1
	res := 0
	leftMax, rightMax := 0, 0

	for left < right {
		if height[left] < height[right] {
			if height[left] >= leftMax {
				leftMax = height[left]
			} else {
				res += (leftMax - height[left])
			}
			left++
		} else {
			if height[right] >= rightMax {
				rightMax = height[right]
			} else {
				res += (rightMax - height[right])
			}
			right--
		}
	}

	return res
}
