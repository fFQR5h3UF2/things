// Submission title: for Rotate Array
// Submission url  : https://leetcode.com/submissions/detail/692284664/
// Submission json : {"id": 692284664, "status_display": "Accepted", "lang": "golang", "question_id": 189, "title_slug": "rotate-array", "code": "\nfunc rotate(numbers []int, steps int) {\n\tlength := len(numbers)\n\t// removing unnecessary steps\n\tif steps >= length {\n\t\tsteps %= length\n\t}\n\t// checking edge cases\n\tif length == 1 || steps == 0 {\n\t\treturn\n\t}\n\tremainder, rotation_start := make([]int, steps), length-steps\n\t// copy everything that needs to be shifted to another array\n\tcopy(remainder, numbers[rotation_start:])\n\t// move everything to the right\n\tcopy(numbers[steps:], numbers[0:rotation_start])\n\t// move shifted elements to the beginning\n\tcopy(numbers[0:steps], remainder)\n}\n", "title": "Rotate Array", "url": "/submissions/detail/692284664/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651580931, "status": 10, "runtime": "57 ms", "is_pending": "Not Pending", "memory": "9.1 MB", "compare_result": "11111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func rotate(numbers []int, steps int) {
	length := len(numbers)
	// removing unnecessary steps
	if steps >= length {
		steps %= length
	}
	// checking edge cases
	if length == 1 || steps == 0 {
		return
	}
	remainder, rotation_start := make([]int, steps), length-steps
	// copy everything that needs to be shifted to another array
	copy(remainder, numbers[rotation_start:])
	// move everything to the right
	copy(numbers[steps:], numbers[0:rotation_start])
	// move shifted elements to the beginning
	copy(numbers[0:steps], remainder)
}
