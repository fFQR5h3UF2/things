// Submission title: Number of 1 Bits
// Submission url  : https://leetcode.com/problems/number-of-1-bits/description/
// Submission url  : https://leetcode.com/submissions/detail/692709119/
// Submission json : {"id":692709119,"status_display":"Accepted","lang":"golang","question_id":191,"title_slug":"number-of-1-bits","code":"\nfunc hammingWeight(number uint32) (result int) {\n\tfor number > 0 {\n\t\tif number&1 != 0 {\n\t\t\tresult++\n\t\t}\n\t\tnumber >>= 1\n\t}\n\treturn\n}\n","title":"Number of 1 Bits","url":"/submissions/detail/692709119/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651632550,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"2 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func hammingWeight(number uint32) (result int) {
	for number > 0 {
		if number&1 != 0 {
			result++
		}
		number >>= 1
	}
	return
}