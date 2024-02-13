// Submission title: Reverse String
// Submission url  : https://leetcode.com/problems/reverse-string/description/
// Submission url  : https://leetcode.com/submissions/detail/693609237/
// Submission json : {"id":693609237,"status_display":"Accepted","lang":"golang","question_id":344,"title_slug":"reverse-string","code":"func reverseString(characters []byte) {\n\tlength := len(characters)\n\tfor index := 0; index < length/2; index++ {\n\t\tindex_last := length - index -1 \n\t\tcurrent, last := characters[index], characters[index_last]\n\t\tcharacters[index_last] = current\n\t\tcharacters[index] = last\n\t}\n}\n","title":"Reverse String","url":"/submissions/detail/693609237/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651747832,"status":10,"runtime":"38 ms","is_pending":"Not Pending","memory":"6.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func reverseString(characters []byte) {
	length := len(characters)
	for index := 0; index < length/2; index++ {
		index_last := length - index - 1
		current, last := characters[index], characters[index_last]
		characters[index_last] = current
		characters[index] = last
	}
}
