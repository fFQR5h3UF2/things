// Submission for Search Insert Position
// Submission url: https://leetcode.com/submissions/detail/691666996/

package submissions


func searchInsert(numbers []int, target int) int {
	// checking edge cases
	length := len(numbers)
	if numbers[0] == target {
		return 0
	} else if numbers[length-1] == target {
		return length - 1
	}
	left, right := 1, length-1
	index := left + (right-left)/2
	number := numbers[index]
	for right >= left {
		// overflow protection
		index = left + (right-left)/2
		number = numbers[index]
		switch {
		case number == target:
			// found the target
			return index
		case number > target:
			// the number is bigger -> the target is to the left -> discard right
			right = index - 1
		case number < target:
			// the number is smaller -> the target is to the right -> discard left
			left = index + 1
		}
	}
	// the target is not in the array
	if number > target {
		return index
	}
	return index + 1
}
