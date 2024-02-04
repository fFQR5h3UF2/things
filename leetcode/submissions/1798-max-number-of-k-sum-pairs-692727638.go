// Submission for Max Number of K-Sum Pairs
// Submission url: https://leetcode.com/submissions/detail/692727638/

package submissions


func maxOperations(numbers []int, sum int) int {
	count, previous := 0, make(map[int]int, len(numbers))
	for _, current := range numbers {
		index_target := sum - current
		target_unmatched, target_occured := previous[index_target]
		// if the current number has not occured before, then it is not in the map
		// -> it needs to be initialized
		if _, current_occured := previous[current]; !current_occured {
			previous[current] = 0
		}
		// number of duplicates of the current number has increased
		previous[current]++
		switch {
		case !target_occured:
			// in order to get the sum we need the target, but it has not appeared yet
			continue
		case target_occured && target_unmatched > 0:
			// the target has appeared before and there are some unmached duplicates left
			// -> removing the current number and the target from possible matches
			previous[current]--
			previous[index_target]--
			count++
		case target_occured && target_unmatched == 0:
			// the target has occured before but there are not unmatched duplicates
			// -> adding the current number to matches
			previous[current]++
		}
	}
	return count
}
