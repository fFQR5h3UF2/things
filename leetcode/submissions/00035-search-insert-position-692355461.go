// Submission title: for Search Insert Position
// Submission url  : https://leetcode.com/submissions/detail/692355461/
// Submission json : {"id": 692355461, "status_display": "Accepted", "lang": "golang", "question_id": 35, "title_slug": "search-insert-position", "code": "func searchInsert(numbers []int, target int) int {\n\t// checking edge cases\n\tlength := len(numbers)\n\tif numbers[0] == target {\n\t\treturn 0\n\t} else if numbers[length-1] == target {\n\t\treturn length - 1\n\t}\n\tleft, right, index, was_bigger := 0, length-1, 0, false\n\tfor right >= left {\n\t\t// overflow protection\n\t\tindex = left + (right-left)/2\n\t\tnumber := numbers[index]\n\t\t//fmt.Println(\"index\", index, \"left\", left, \"right\", right)\n\t\tswitch {\n\t\tcase number == target:\n\t\t\t// found the target\n\t\t\treturn index\n\t\tcase number > target:\n\t\t\t// the number is bigger -> the target is to the left -> discard right\n\t\t\tright = index - 1\n\t\t\twas_bigger = true\n\t\tcase number < target:\n\t\t\t// the number is smaller -> the target is to the right -> discard left\n\t\t\tleft = index + 1\n\t\t\twas_bigger = false\n\t\t}\n\t}\n\t// the target is not in the array\n\n\t// the last number was bigger -> target should be to the left\n\tif was_bigger {\n\t\treturn index\n\t}\n\t// the last number was smaller -> target should be to the right\n\treturn index + 1\n}\n", "title": "Search Insert Position", "url": "/submissions/detail/692355461/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651589068, "status": 10, "runtime": "3 ms", "is_pending": "Not Pending", "memory": "3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func searchInsert(numbers []int, target int) int {
	// checking edge cases
	length := len(numbers)
	if numbers[0] == target {
		return 0
	} else if numbers[length-1] == target {
		return length - 1
	}
	left, right, index, was_bigger := 0, length-1, 0, false
	for right >= left {
		// overflow protection
		index = left + (right-left)/2
		number := numbers[index]
		//fmt.Println("index", index, "left", left, "right", right)
		switch {
		case number == target:
			// found the target
			return index
		case number > target:
			// the number is bigger -> the target is to the left -> discard right
			right = index - 1
			was_bigger = true
		case number < target:
			// the number is smaller -> the target is to the right -> discard left
			left = index + 1
			was_bigger = false
		}
	}
	// the target is not in the array

	// the last number was bigger -> target should be to the left
	if was_bigger {
		return index
	}
	// the last number was smaller -> target should be to the right
	return index + 1
}
