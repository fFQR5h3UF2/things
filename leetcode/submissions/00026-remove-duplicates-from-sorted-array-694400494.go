// Submission title: Remove Duplicates from Sorted Array
// Submission url  : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
// Submission url  : https://leetcode.com/submissions/detail/694400494/
// Submission json : {"id":694400494,"status_display":"Accepted","lang":"golang","question_id":26,"title_slug":"remove-duplicates-from-sorted-array","code":"func removeDuplicates(numbers []int) int {\n\t// ensure there are at least two numbers\n\tlength := len(numbers)\n\tif length == 1 {\n\t\treturn 1\n\t}\n\tindex_non_duplicate := 1\n\tfor index := 1; index < length; index++ {\n\t\tcurrent, previous := numbers[index], numbers[index-1]\n\t\tif current == previous {\n\t\t\t// it is a duplicate - ignore it\n\t\t\tcontinue\n\t\t}\n\t\t// it is not a duplicate -> place it and move the index\n\t\tnumbers[index_non_duplicate] = current\n\t\tindex_non_duplicate++\n\t}\n\treturn index_non_duplicate\n}\n","title":"Remove Duplicates from Sorted Array","url":"/submissions/detail/694400494/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651855838,"status":10,"runtime":"12 ms","is_pending":"Not Pending","memory":"4.5 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func removeDuplicates(numbers []int) int {
	// ensure there are at least two numbers
	length := len(numbers)
	if length == 1 {
		return 1
	}
	index_non_duplicate := 1
	for index := 1; index < length; index++ {
		current, previous := numbers[index], numbers[index-1]
		if current == previous {
			// it is a duplicate - ignore it
			continue
		}
		// it is not a duplicate -> place it and move the index
		numbers[index_non_duplicate] = current
		index_non_duplicate++
	}
	return index_non_duplicate
}
