// Submission for Find Smallest Letter Greater Than Target
// Submission url: https://leetcode.com/submissions/detail/693728508/

package submissions


func nextGreatestLetter(letters []byte, target byte) byte {
	left, right, smallest := 0, len(letters)-1, byte(1)
	for right >= left {
		index := left + (right-left)/2
		character := letters[index]
		// the character is bigger, we found at least one result
		// smaller characters are to the left -> discard right
		if character > target {
			smallest = character
			right = index - 1
			continue
		}
		// character is either equal or smaller -> there is no results to the
		// left -> discard left
		left = index + 1
	}
	return smallest
}
