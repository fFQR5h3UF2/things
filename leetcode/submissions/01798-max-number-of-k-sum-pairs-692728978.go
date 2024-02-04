// Submission title: for Max Number of K-Sum Pairs
// Submission url  : https://leetcode.com/submissions/detail/692728978/
// Submission json : {"id": 692728978, "status_display": "Accepted", "lang": "golang", "question_id": 1798, "title_slug": "max-number-of-k-sum-pairs", "code": "\nfunc maxOperations(numbers []int, sum int) int {\n\tcount, previous := 0, make(map[int]int, len(numbers))\n\tfor _, current := range numbers {\n\t\ttarget := sum - current\n\t\ttarget_unmatched, target_occured := previous[target]\n\t\t// if the current number has not occured before, then it is not in the map\n\t\t// -> it needs to be initialized\n\t\tif _, current_occured := previous[current]; !current_occured {\n\t\t\tprevious[current] = 0\n\t\t}\n\t\t// number of duplicates of the current number has increased\n\t\tprevious[current]++\n\t\tswitch {\n\t\tcase target_occured && target_unmatched == 0:\n\t\t\t// the target has occured before but there are no unmatched duplicates\n\t\t\tfallthrough\n\t\tcase !target_occured:\n\t\t\t// in order to get the sum we need the target, but it has not appeared yet\n\t\t\tcontinue\n\t\tcase target_occured && target_unmatched > 0:\n\t\t\t// the target has appeared before and there are some unmached duplicates left\n\t\t\t// -> removing the current number and the target from possible matches\n\t\t\tprevious[current]--\n\t\t\tprevious[target]--\n\t\t\tcount++\n\t\t}\n\t}\n\treturn count\n}\n", "title": "Max Number of K-Sum Pairs", "url": "/submissions/detail/692728978/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651634783, "status": 10, "runtime": "206 ms", "is_pending": "Not Pending", "memory": "13 MB", "compare_result": "111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func maxOperations(numbers []int, sum int) int {
	count, previous := 0, make(map[int]int, len(numbers))
	for _, current := range numbers {
		target := sum - current
		target_unmatched, target_occured := previous[target]
		// if the current number has not occured before, then it is not in the map
		// -> it needs to be initialized
		if _, current_occured := previous[current]; !current_occured {
			previous[current] = 0
		}
		// number of duplicates of the current number has increased
		previous[current]++
		switch {
		case target_occured && target_unmatched == 0:
			// the target has occured before but there are no unmatched duplicates
			fallthrough
		case !target_occured:
			// in order to get the sum we need the target, but it has not appeared yet
			continue
		case target_occured && target_unmatched > 0:
			// the target has appeared before and there are some unmached duplicates left
			// -> removing the current number and the target from possible matches
			previous[current]--
			previous[target]--
			count++
		}
	}
	return count
}
