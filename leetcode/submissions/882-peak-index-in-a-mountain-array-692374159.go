// Submission for Peak Index in a Mountain Array
// Submission url: https://leetcode.com/submissions/detail/692374159/

package submissions


func peakIndexInMountainArray(array []int) int {
	length := len(array)
	if length == 3 {
		return 1
	}
	left, right, index_highest, index := 0, length-1, 0, 0
	moving_right := true
	for right >= left {
		// overflow protection
		index = left + (right-left)/2
		highest := array[index_highest]
		//fmt.Println(index, highest)
		number := array[index]
		switch {
		case !moving_right && number < highest:
			// number is smaller and we are moving to the left
			// -> discard left, switch direction
			moving_right = true
			left = index + 1
		case moving_right && number >= highest:
			// number is bigger and we are moving to the right -> discard left
			left = index + 1
			index_highest = index
		case moving_right && number < highest:
			// number is smaller and we are moving to the right
			// -> discard right, switch direction
			moving_right = false
			right = index - 1
		case !moving_right && number >= highest:
			// number is bigger and we are moving to the left -> discard right
			right = index - 1
			index_highest = index
		}
	}
	return index_highest
}
