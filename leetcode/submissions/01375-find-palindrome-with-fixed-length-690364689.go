// Submission title: Find Palindrome With Fixed Length
// Submission url  : https://leetcode.com/problems/find-palindrome-with-fixed-length/description/
// Submission url  : https://leetcode.com/submissions/detail/690364689/
// Submission json : {"id":690364689,"status_display":"Accepted","lang":"golang","question_id":1375,"title_slug":"find-palindrome-with-fixed-length","code":"func kthPalindrome(queries []int, intLength int) (answer []int64) {\n\tfor _, query := range queries {\n\t\tanswer = append(answer, getPalindrom(query, intLength))\n\t}\n\treturn\n}\n\nfunc getPalindrom(query int, length int) (result int64) {\n\tis_even := (length & 1) == 0\n\tpower := length / 2\n\tif is_even {\n\t\tpower -= 1\n\t}\n\tpalindrome := int64(math.Pow10(power)) + int64(query) - 1\n\tresult = palindrome\n\tif !is_even {\n\t\tpalindrome /= 10\n\t}\n\tfor palindrome > 0 {\n\t\tresult = result*10 + palindrome%10\n\t\tpalindrome /= 10\n\t}\n\tif len(fmt.Sprint(result)) != length {\n\t\treturn -1\n\t}\n\treturn\n}\n","title":"Find Palindrome With Fixed Length","url":"/submissions/detail/690364689/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651339623,"status":10,"runtime":"151 ms","is_pending":"Not Pending","memory":"9.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func kthPalindrome(queries []int, intLength int) (answer []int64) {
	for _, query := range queries {
		answer = append(answer, getPalindrom(query, intLength))
	}
	return
}

func getPalindrom(query int, length int) (result int64) {
	is_even := (length & 1) == 0
	power := length / 2
	if is_even {
		power -= 1
	}
	palindrome := int64(math.Pow10(power)) + int64(query) - 1
	result = palindrome
	if !is_even {
		palindrome /= 10
	}
	for palindrome > 0 {
		result = result*10 + palindrome%10
		palindrome /= 10
	}
	if len(fmt.Sprint(result)) != length {
		return -1
	}
	return
}
