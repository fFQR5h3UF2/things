// Submission title: for Reverse Words in a String III
// Submission url  : https://leetcode.com/submissions/detail/693639118/
// Submission json : {"id": 693639118, "status_display": "Accepted", "lang": "golang", "question_id": 557, "title_slug": "reverse-words-in-a-string-iii", "code": "func reverseWords(_string string) string {\n\tindex_word_start, length, result := 0, len(_string), []rune(_string)\n\tfor index, character := range result {\n\t\t// ignore normal characters\n\t\tif character != ' ' {\n\t\t\tcontinue\n\t\t}\n\t\t// word ended -> reverse characters from the start of the word to the\n\t\t//end of it\n\t\treverse_word(result, length, index_word_start, index)\n\t\tindex_word_start = index + 1\n\t}\n\treverse_word(result, length, index_word_start, length)\n\treturn string(result)\n}\n\nfunc reverse_word(_string []rune, length int, start int, end int) {\n\t//fmt.Println(\"reversing\", string(_string), start, \"->\", end)\n\tlength_word := end - start\n\tfor index := start; index < start+length_word/2; index++ {\n\t\tindex_last := end - (index - start) - 1\n\t\tcurrent, last := _string[index], _string[index_last]\n\t\t_string[index], _string[index_last] = last, current\n\t}\n\t//fmt.Println(\"result\", string(_string), start, \"->\", end)\n}\n", "title": "Reverse Words in a String III", "url": "/submissions/detail/693639118/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651752654, "status": 10, "runtime": "5 ms", "is_pending": "Not Pending", "memory": "6.4 MB", "compare_result": "11111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func reverseWords(_string string) string {
	index_word_start, length, result := 0, len(_string), []rune(_string)
	for index, character := range result {
		// ignore normal characters
		if character != ' ' {
			continue
		}
		// word ended -> reverse characters from the start of the word to the
		//end of it
		reverse_word(result, length, index_word_start, index)
		index_word_start = index + 1
	}
	reverse_word(result, length, index_word_start, length)
	return string(result)
}

func reverse_word(_string []rune, length int, start int, end int) {
	//fmt.Println("reversing", string(_string), start, "->", end)
	length_word := end - start
	for index := start; index < start+length_word/2; index++ {
		index_last := end - (index - start) - 1
		current, last := _string[index], _string[index_last]
		_string[index], _string[index_last] = last, current
	}
	//fmt.Println("result", string(_string), start, "->", end)
}
