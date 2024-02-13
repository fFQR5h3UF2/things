// Submission title: Substring with Concatenation of All Words
// Submission url  : https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
// Submission url  : https://leetcode.com/submissions/detail/1091199226/
// Submission json : {"id":1091199226,"status_display":"Accepted","lang":"golang","question_id":30,"title_slug":"substring-with-concatenation-of-all-words","code":"func findSubstring(s string, words []string) []int {\n    \n    wordLen := len(words[0])\n    totalWords := len(words)\n    mem := make(map[string]int, totalWords)\n    \n    \n    for _, str := range words {\n        mem[str] += 1\n    }\n    \n    temp := make(map[string]int, totalWords)\n    var found bool\n    result := make([]int, 0)\n    \n    for i:=0; i + wordLen*totalWords <= len(s);  {\n            \n        found = true\n        temp = make(map[string]int, totalWords)\n\n        for j := i; j < i + wordLen*totalWords; j += wordLen {\n            if _, ok := mem[ s[j:j+wordLen] ]; ok {\n                temp[ s[j:j+wordLen] ] += 1\n            } else {\n                found = false\n                break\n            }\n        }\n\n        if found {\n            for key, _ := range mem {\n                if val, ok := temp[key]; !ok || val != mem[key]{\n                    i++\n                    found = false\n                    break\n                }\n            }\n\n            if found {\n                result = append(result, i)\n                i += 1    \n            }\n\n        } else {\n            i++\n        }\n    }\n    \n    return result\n    \n}","title":"Substring with Concatenation of All Words","url":"/submissions/detail/1091199226/","lang_name":"Go","time":"3 months","timestamp":1699093498,"status":10,"runtime":"846 ms","is_pending":"Not Pending","memory":"13.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func findSubstring(s string, words []string) []int {

	wordLen := len(words[0])
	totalWords := len(words)
	mem := make(map[string]int, totalWords)

	for _, str := range words {
		mem[str] += 1
	}

	temp := make(map[string]int, totalWords)
	var found bool
	result := make([]int, 0)

	for i := 0; i+wordLen*totalWords <= len(s); {

		found = true
		temp = make(map[string]int, totalWords)

		for j := i; j < i+wordLen*totalWords; j += wordLen {
			if _, ok := mem[s[j:j+wordLen]]; ok {
				temp[s[j:j+wordLen]] += 1
			} else {
				found = false
				break
			}
		}

		if found {
			for key, _ := range mem {
				if val, ok := temp[key]; !ok || val != mem[key] {
					i++
					found = false
					break
				}
			}

			if found {
				result = append(result, i)
				i += 1
			}

		} else {
			i++
		}
	}

	return result

}
