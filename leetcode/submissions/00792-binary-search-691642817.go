// Submission title: for Binary Search
// Submission url  : https://leetcode.com/submissions/detail/691642817/
// Submission json : {"id": 691642817, "status_display": "Accepted", "lang": "golang", "question_id": 792, "title_slug": "binary-search", "code": "/* https://leetcode.com/problems/binary-search/\n\nGiven an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.\n\nYou must write an algorithm with O(log n) runtime complexity.\n\n\n\nExample 1:\n\nInput: nums = [-1,0,3,5,9,12], target = 9\nOutput: 4\nExplanation: 9 exists in nums and its index is 4\n\nExample 2:\n\nInput: nums = [-1,0,3,5,9,12], target = 2\nOutput: -1\nExplanation: 2 does not exist in nums so return -1\n\n\n\nConstraints:\n\n    1 <= nums.length <= 104\n    -104 < nums[i], target < 104\n    All the integers in nums are unique.\n    nums is sorted in ascending order.\n\n*/\npackage main\n\nfunc search(numbers []int, target int) int {\n\tlength := len(numbers)\n\tswitch {\n\tcase numbers[0] > target:\n\t\t// smallet number > target = there is no target in the array\n\t\tfallthrough\n\tcase numbers[length-1] < target:\n\t\t// biggest number < target = there is no target in the array\n\t\treturn -1\n\tcase numbers[length-1] == target:\n\t\t// checking just in case, can save time\n\t\treturn length - 1\n\tcase numbers[0] == target:\n\t\t// checking just in case, can save time\n\t\treturn 0\n\t}\n\n\tleft, right := 0, length-1\n\tfor right >= left {\n\t\t// overflow protection\n\t\tindex := left + (right-left)/2\n\t\tnumber := numbers[index]\n\t\tswitch {\n\t\tcase number == target:\n\t\t\t// found the target\n\t\t\treturn index\n\t\tcase number > target:\n\t\t\t// array is in the ascending order, the number is bigger\n\t\t\t// -> the target is to the left -> discard right\n\t\t\tright = index - 1\n\t\tcase number < target:\n\t\t\t// array is in the ascending order, the number is smaller\n\t\t\t// -> the target is to the right -> discard left\n\t\t\tleft = index + 1\n\t\t}\n\t}\n\t// search space is empty, there is no target\n\treturn -1\n}\n", "title": "Binary Search", "url": "/submissions/detail/691642817/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651502044, "status": 10, "runtime": "64 ms", "is_pending": "Not Pending", "memory": "6.9 MB", "compare_result": "11111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

/* https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1



Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.

*/

func search(numbers []int, target int) int {
	length := len(numbers)
	switch {
	case numbers[0] > target:
		// smallet number > target = there is no target in the array
		fallthrough
	case numbers[length-1] < target:
		// biggest number < target = there is no target in the array
		return -1
	case numbers[length-1] == target:
		// checking just in case, can save time
		return length - 1
	case numbers[0] == target:
		// checking just in case, can save time
		return 0
	}

	left, right := 0, length-1
	for right >= left {
		// overflow protection
		index := left + (right-left)/2
		number := numbers[index]
		switch {
		case number == target:
			// found the target
			return index
		case number > target:
			// array is in the ascending order, the number is bigger
			// -> the target is to the left -> discard right
			right = index - 1
		case number < target:
			// array is in the ascending order, the number is smaller
			// -> the target is to the right -> discard left
			left = index + 1
		}
	}
	// search space is empty, there is no target
	return -1
}
