// Submission title: Two Sum II - Input Array Is Sorted
// Submission url  : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
// Submission url  : https://leetcode.com/submissions/detail/690000287/
// Submission json : {"id":690000287,"status_display":"Accepted","lang":"golang","question_id":167,"title_slug":"two-sum-ii-input-array-is-sorted","code":"func twoSum(numbers []int, target int) []int {\n\tnumbers_len := len(numbers)\n\tfor index, number := range numbers {\n\t\tfor index_inner := index + 1; index_inner < numbers_len; index_inner++ {\n\t\t\tif numbers[index_inner]+number == target {\n\t\t\t\treturn []int{index + 1, index_inner + 1}\n\t\t\t}\n\t\t}\n\t}\n\treturn []int{}\n}\n","title":"Two Sum II - Input Array Is Sorted","url":"/submissions/detail/690000287/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651290083,"status":10,"runtime":"438 ms","is_pending":"Not Pending","memory":"5.4 MB","compare_result":"111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func twoSum(numbers []int, target int) []int {
	numbers_len := len(numbers)
	for index, number := range numbers {
		for index_inner := index + 1; index_inner < numbers_len; index_inner++ {
			if numbers[index_inner]+number == target {
				return []int{index + 1, index_inner + 1}
			}
		}
	}
	return []int{}
}
