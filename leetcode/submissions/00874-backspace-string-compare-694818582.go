// Submission title: Backspace String Compare
// Submission url  : https://leetcode.com/problems/backspace-string-compare/description/
// Submission url  : https://leetcode.com/submissions/detail/694818582/
// Submission json : {"id":694818582,"status_display":"Accepted","lang":"golang","question_id":874,"title_slug":"backspace-string-compare","code":"\nfunc backspaceCompare(string_1 string, string_2 string) bool {\n\tlength_1, length_2 := len(string_1), len(string_2)\n\tlist_1, list_2, length_biggest := list.List{}, list.List{}, length_1\n\tif length_2 > length_1 {\n\t\tlength_biggest = length_2\n\t}\n\tfor index := 0; index < length_biggest; index++ {\n\t\tif index < length_1 {\n\t\t\tbackspace_action(&list_1, string_1[index])\n\t\t}\n\t\tif index < length_2 {\n\t\t\tbackspace_action(&list_2, string_2[index])\n\t\t}\n\t}\n\t// lists are not equal, there is no need to check\n\tif list_1.Len() != list_2.Len() {\n\t\treturn false\n\t}\n\t// checking elements after all deletions\n\telement_1, element_2 := list_1.Back(), list_2.Back()\n\tfor element_1 != nil {\n\t\tif element_1.Value != element_2.Value {\n\t\t\t// elements are not equal -> strings are not equal\n\t\t\treturn false\n\t\t}\n\t\telement_1, element_2 = element_1.Next(), element_2.Next()\n\t}\n\t// checked all elements, strings are equal\n\treturn true\n}\n\nfunc backspace_action(list *list.List, character byte) {\n\tswitch {\n\tcase character == '#' && list.Len() != 0:\n\t\t// delete last character\n\t\tlist.Remove(list.Front())\n\t\tfallthrough\n\tcase character == '#' && list.Len() == 0:\n\t\t// just return if the list is empty\n\t\treturn\n\t}\n\tlist.PushFront(character)\n}\n","title":"Backspace String Compare","url":"/submissions/detail/694818582/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651917913,"status":10,"runtime":"5 ms","is_pending":"Not Pending","memory":"2.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func backspaceCompare(string_1 string, string_2 string) bool {
	length_1, length_2 := len(string_1), len(string_2)
	list_1, list_2, length_biggest := list.List{}, list.List{}, length_1
	if length_2 > length_1 {
		length_biggest = length_2
	}
	for index := 0; index < length_biggest; index++ {
		if index < length_1 {
			backspace_action(&list_1, string_1[index])
		}
		if index < length_2 {
			backspace_action(&list_2, string_2[index])
		}
	}
	// lists are not equal, there is no need to check
	if list_1.Len() != list_2.Len() {
		return false
	}
	// checking elements after all deletions
	element_1, element_2 := list_1.Back(), list_2.Back()
	for element_1 != nil {
		if element_1.Value != element_2.Value {
			// elements are not equal -> strings are not equal
			return false
		}
		element_1, element_2 = element_1.Next(), element_2.Next()
	}
	// checked all elements, strings are equal
	return true
}

func backspace_action(list *list.List, character byte) {
	switch {
	case character == '#' && list.Len() != 0:
		// delete last character
		list.Remove(list.Front())
		fallthrough
	case character == '#' && list.Len() == 0:
		// just return if the list is empty
		return
	}
	list.PushFront(character)
}
