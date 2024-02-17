// Submission title: Substring with Concatenation of All Words
// Submission url  : https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/"
// Submission url  : https://leetcode.com/submissions/detail/1091199226/"
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
