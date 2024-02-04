// Submission for Peak Index in a Mountain Array
// Submission url: https://leetcode.com/submissions/detail/692383619/

package submissions

func peakIndexInMountainArray(array []int) int {
	left, right := 0, len(array)-1
	for right > left {
		// overflow protection
		index := left + (right-left)/2
		// next element is bigger -> top is to the right -> discard left
		if array[index+1] > array[index] {
			left = index + 1
			continue
		}
		// next element is equal or smaller -> discard right
		// 'index' could be the answer, so it should not be discarded
		right = index
	}
	return right
}
