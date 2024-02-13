// Submission title: 132 Pattern
// Submission url  : https://leetcode.com/problems/132-pattern/description/
// Submission url  : https://leetcode.com/submissions/detail/694834562/
// Submission json : {"id":694834562,"status_display":"Accepted","lang":"golang","question_id":456,"title_slug":"132-pattern","code":"\nfunc find132pattern(numbers []int) bool {\n\tlength := len(numbers)\n\tif length < 3 {\n\t\t// if the array doesn't have at least three numbers, it cannot have\n\t\t// '123' pattern\n\t\treturn false\n\t}\n\tlist, third_element := list.List{}, math.MinInt\n\tfor index := length - 1; index >= 0; index-- {\n\t\tcurrent := numbers[index]\n\t\tif current < third_element {\n\t\t\treturn true\n\t\t}\n\t\tfor list.Len() != 0 && list.Front().Value.(int) < current {\n\t\t\tthird_element = list.Front().Value.(int)\n\t\t\tlist.Remove(list.Front())\n\t\t}\n\t\tlist.PushFront(current)\n\t}\n\treturn false\n}","title":"132 Pattern","url":"/submissions/detail/694834562/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651920255,"status":10,"runtime":"95 ms","is_pending":"Not Pending","memory":"12.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func find132pattern(numbers []int) bool {
	length := len(numbers)
	if length < 3 {
		// if the array doesn't have at least three numbers, it cannot have
		// '123' pattern
		return false
	}
	list, third_element := list.List{}, math.MinInt
	for index := length - 1; index >= 0; index-- {
		current := numbers[index]
		if current < third_element {
			return true
		}
		for list.Len() != 0 && list.Front().Value.(int) < current {
			third_element = list.Front().Value.(int)
			list.Remove(list.Front())
		}
		list.PushFront(current)
	}
	return false
}
