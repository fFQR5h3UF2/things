// Submission title: Find the Distance Value Between Two Arrays
// Submission url  : https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
// Submission url  : https://leetcode.com/submissions/detail/692797975/
// Submission json : {"id":692797975,"status_display":"Accepted","lang":"golang","question_id":1486,"title_slug":"find-the-distance-value-between-two-arrays","code":"\nfunc findTheDistanceValue(array_1 []int, array_2 []int, target int) int {\n\t// sorting it to use binary search\n\tsort.Ints(array_2)\n\tlength_2, count := len(array_2), 0\n\tfor _, current_1 := range array_1 {\n\t\tleft, right, add_to_count := 0, length_2-1, true\n\t\tfor right >= left {\n\t\t\tindex := left + (right-left)/2\n\t\t\tcurrent_2 := array_2[index]\n\t\t\tif abs(current_1, current_2) <= target {\n\t\t\t\t// current_1 is inside |arr1[i]-arr2[j]| <= d\n\t\t\t\t// -> ignore it\n\t\t\t\tadd_to_count = false\n\t\t\t\tbreak\n\t\t\t}\n\t\t\tswitch {\n\t\t\tcase current_2 > current_1:\n\t\t\t\t// current_2 is bigger than current_1\n\t\t\t\t// -> all numbers to the right are bigger\n\t\t\t\t// -> discard right, add to count\n\t\t\t\tright = index - 1\n\t\t\tcase current_2 < current_1:\n\t\t\t\t// current_2 is smaller than current_1\n\t\t\t\t// -> all numbers to the left are smaller\n\t\t\t\t// -> discard left, add to count\n\t\t\t\tleft = index + 1\n\t\t\t}\n\t\t}\n\t\tif add_to_count {\n\t\t\tcount++\n\t\t}\n\t}\n\treturn count\n}\n\nfunc abs(number_1 int, number_2 int) int {\n\tdifference := number_1 - number_2\n\tif difference < 0 {\n\t\treturn difference * -1\n\t}\n\treturn difference\n}\n","title":"Find the Distance Value Between Two Arrays","url":"/submissions/detail/692797975/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651642220,"status":10,"runtime":"5 ms","is_pending":"Not Pending","memory":"3.9 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func findTheDistanceValue(array_1 []int, array_2 []int, target int) int {
	// sorting it to use binary search
	sort.Ints(array_2)
	length_2, count := len(array_2), 0
	for _, current_1 := range array_1 {
		left, right, add_to_count := 0, length_2-1, true
		for right >= left {
			index := left + (right-left)/2
			current_2 := array_2[index]
			if abs(current_1, current_2) <= target {
				// current_1 is inside |arr1[i]-arr2[j]| <= d
				// -> ignore it
				add_to_count = false
				break
			}
			switch {
			case current_2 > current_1:
				// current_2 is bigger than current_1
				// -> all numbers to the right are bigger
				// -> discard right, add to count
				right = index - 1
			case current_2 < current_1:
				// current_2 is smaller than current_1
				// -> all numbers to the left are smaller
				// -> discard left, add to count
				left = index + 1
			}
		}
		if add_to_count {
			count++
		}
	}
	return count
}

func abs(number_1 int, number_2 int) int {
	difference := number_1 - number_2
	if difference < 0 {
		return difference * -1
	}
	return difference
}
