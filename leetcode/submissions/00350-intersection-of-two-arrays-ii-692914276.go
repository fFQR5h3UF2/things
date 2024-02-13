// Submission title: Intersection of Two Arrays II
// Submission url  : https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
// Submission url  : https://leetcode.com/submissions/detail/692914276/
// Submission json : {"id":692914276,"status_display":"Accepted","lang":"golang","question_id":350,"title_slug":"intersection-of-two-arrays-ii","code":"\nfunc intersect(numbers_1 []int, numbers_2 []int) []int {\n\tlength_1, length_2 := len(numbers_1), len(numbers_2)\n\tlength_biggest, result := length_1, make([]int, length_1+length_2)\n\tif length_2 > length_1 {\n\t\tlength_biggest = length_2\n\t}\n\toccurences := make(map[int][]int, length_biggest)\n\n\tfor index := 0; index < length_biggest; index++ {\n\t\tif index < length_1 {\n\t\t\tadd_to_occurences(numbers_1[index], 0, occurences)\n\t\t}\n\t\tif index < length_2 {\n\t\t\tadd_to_occurences(numbers_2[index], 1, occurences)\n\t\t}\n\t}\n\tindex := 0\n\tfor number, occurence := range occurences {\n\t\trepeat := occurence[0]\n\t\tif occurence[1] < repeat {\n\t\t\trepeat = occurence[1]\n\t\t}\n\t\tfor ; repeat > 0; repeat-- {\n\t\t\tresult[index] = number\n\t\t\tindex++\n\t\t}\n\t}\n    return result[0 : index]\n}\nfunc add_to_occurences(number int, index int, occurences map[int][]int) {\n\tif _, occured := occurences[number]; !occured {\n\t\toccurences[number] = make([]int, 2)\n\t}\n\toccurences[number][index]++\n}\n","title":"Intersection of Two Arrays II","url":"/submissions/detail/692914276/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651656998,"status":10,"runtime":"4 ms","is_pending":"Not Pending","memory":"3.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func intersect(numbers_1 []int, numbers_2 []int) []int {
	length_1, length_2 := len(numbers_1), len(numbers_2)
	length_biggest, result := length_1, make([]int, length_1+length_2)
	if length_2 > length_1 {
		length_biggest = length_2
	}
	occurences := make(map[int][]int, length_biggest)

	for index := 0; index < length_biggest; index++ {
		if index < length_1 {
			add_to_occurences(numbers_1[index], 0, occurences)
		}
		if index < length_2 {
			add_to_occurences(numbers_2[index], 1, occurences)
		}
	}
	index := 0
	for number, occurence := range occurences {
		repeat := occurence[0]
		if occurence[1] < repeat {
			repeat = occurence[1]
		}
		for ; repeat > 0; repeat-- {
			result[index] = number
			index++
		}
	}
	return result[0:index]
}
func add_to_occurences(number int, index int, occurences map[int][]int) {
	if _, occured := occurences[number]; !occured {
		occurences[number] = make([]int, 2)
	}
	occurences[number][index]++
}
