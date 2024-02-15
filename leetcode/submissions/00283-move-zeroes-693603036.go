// Submission title: Move Zeroes
// Submission url  : https://leetcode.com/problems/move-zeroes/description/
// Submission url  : https://leetcode.com/submissions/detail/693603036/
// Submission json : {"id":693603036,"status_display":"Accepted","lang":"golang","question_id":283,"title_slug":"move-zeroes","code":"\nfunc moveZeroes(numbers []int) {\n\tindex_zero := -1\n\t// sliding window algorithm\n\tfor index, number := range numbers {\n\t\t// if index_zero is not set, then the first zero is index_zero\n\t\tif index_zero == -1 && number == 0 {\n\t\t\tindex_zero = index\n\t\t}\n\t\t// there is no need to move numbers if there were no zeros before\n\t\t// there is no need to move zeros\n\t\tif index_zero == -1 || number == 0 {\n\t\t\tcontinue\n\t\t}\n\t\t// after some zeros we encounter a non-zero number\n\t\t// moving that number to the beginning of zeros\n\t\tnumbers[index_zero] = number\n\t\t// current number becomes zero\n\t\tnumbers[index] = 0\n\t\t// moving the index\n\t\tindex_zero++\n\t}\n}\n","title":"Move Zeroes","url":"/submissions/detail/693603036/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651746777,"status":10,"runtime":"20 ms","is_pending":"Not Pending","memory":"7.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func moveZeroes(numbers []int) {
	index_zero := -1
	// sliding window algorithm
	for index, number := range numbers {
		// if index_zero is not set, then the first zero is index_zero
		if index_zero == -1 && number == 0 {
			index_zero = index
		}
		// there is no need to move numbers if there were no zeros before
		// there is no need to move zeros
		if index_zero == -1 || number == 0 {
			continue
		}
		// after some zeros we encounter a non-zero number
		// moving that number to the beginning of zeros
		numbers[index_zero] = number
		// current number becomes zero
		numbers[index] = 0
		// moving the index
		index_zero++
	}
}