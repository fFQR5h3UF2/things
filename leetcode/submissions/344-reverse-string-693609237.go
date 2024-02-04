# Submission for 'Reverse String'
# Submission url: https://leetcode.com/submissions/detail/693609237/

func reverseString(characters []byte) {
	length := len(characters)
	for index := 0; index < length/2; index++ {
		index_last := length - index -1
		current, last := characters[index], characters[index_last]
		characters[index_last] = current
		characters[index] = last
	}
}
