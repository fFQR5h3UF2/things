// Submission title: Peak Index in a Mountain Array
// Submission url  : https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
// Submission url  : https://leetcode.com/submissions/detail/692383619/
// Submission json : {"id":692383619,"status_display":"Accepted","lang":"golang","question_id":882,"title_slug":"peak-index-in-a-mountain-array","code":"\nfunc peakIndexInMountainArray(array []int) int {\n\tleft, right := 0, len(array)-1\n\tfor right > left {\n\t\t// overflow protection\n\t\tindex := left + (right-left)/2\n\t\t// next element is bigger -> top is to the right -> discard left\n\t\tif array[index+1] > array[index] {\n\t\t\tleft = index + 1\n\t\t\tcontinue\n\t\t}\n\t\t// next element is equal or smaller -> discard right\n\t\t// 'index' could be the answer, so it should not be discarded\n\t\tright = index\n\t}\n\treturn right\n}","title":"Peak Index in a Mountain Array","url":"/submissions/detail/692383619/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651592043,"status":10,"runtime":"17 ms","is_pending":"Not Pending","memory":"4.7 MB","compare_result":"11111111111111111111111111111111111","has_notes":false,"flag_type":1}
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
