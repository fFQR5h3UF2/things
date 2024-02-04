// Submission for Contains Duplicate
// Submission url: https://leetcode.com/submissions/detail/691371448/

package submissions


func containsDuplicate(numbers []int) bool {
	if len(numbers) == 0 || len(numbers) == 1 {
		return false
	}
	occured := make(map[int]bool)
	for _, number := range numbers {
		_, isDuplicate := occured[number]
		if isDuplicate {
			return true
		}
		occured[number] = true
	}
	return false
}
