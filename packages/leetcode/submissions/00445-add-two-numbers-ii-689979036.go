// Submission title: for Add Two Numbers II
// Submission url  : https://leetcode.com/submissions/detail/689979036/
// Submission json : {"id": 689979036, "status_display": "Accepted", "lang": "golang", "question_id": 445, "title_slug": "add-two-numbers-ii", "code": "func reverse(list *ListNode) *ListNode {\n\tif list == nil || list.Next == nil {\n\t\treturn list\n\t}\n\tresult := &ListNode{list.Val, nil}\n\tcurrent := list.Next\n\tfor {\n\t\tif current == nil {\n\t\t\treturn result\n\t\t}\n\t\tresult = &ListNode{current.Val, result}\n        current = current.Next\n\t}\n}\n\nfunc addTwoNumbers(list_1 *ListNode, list_2 *ListNode) *ListNode {\n\tcurrent_1, current_2, result := reverse(list_1), reverse(list_2), &ListNode{}\n\tvar carry int\n\tresult_current := result\n\tfor {\n\t\tvar value_1, value_2 int\n\t\tif current_1 != nil {\n\t\t\tvalue_1 = current_1.Val\n\t\t\tcurrent_1 = current_1.Next\n\t\t}\n\t\tif current_2 != nil {\n\t\t\tvalue_2 = current_2.Val\n\t\t\tcurrent_2 = current_2.Next\n\t\t}\n\t\tsum := value_1 + value_2 + carry\n\t\tif sum > 9 {\n\t\t\tsum -= 10\n\t\t\tcarry = 1\n\t\t} else {\n\t\t\tcarry = 0\n\t\t}\n\t\tresult_current.Val = sum\n\t\tif current_1 == nil && current_2 == nil && carry == 0 {\n\t\t\tresult_current.Next = nil\n\t\t\treturn reverse(result)\n\t\t} else if current_1 == nil && current_2 == nil && carry != 0 {\n\t\t\tcurrent_1 = &ListNode{}\n\t\t}\n\t\tresult_current.Next = &ListNode{}\n\t\tresult_current = result_current.Next\n\t}\n}\n", "title": "Add Two Numbers II", "url": "/submissions/detail/689979036/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651286163, "status": 10, "runtime": "16 ms", "is_pending": "Not Pending", "memory": "5.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func reverse(list *ListNode) *ListNode {
	if list == nil || list.Next == nil {
		return list
	}
	result := &ListNode{list.Val, nil}
	current := list.Next
	for {
		if current == nil {
			return result
		}
		result = &ListNode{current.Val, result}
		current = current.Next
	}
}

func addTwoNumbers(list_1 *ListNode, list_2 *ListNode) *ListNode {
	current_1, current_2, result := reverse(list_1), reverse(list_2), &ListNode{}
	var carry int
	result_current := result
	for {
		var value_1, value_2 int
		if current_1 != nil {
			value_1 = current_1.Val
			current_1 = current_1.Next
		}
		if current_2 != nil {
			value_2 = current_2.Val
			current_2 = current_2.Next
		}
		sum := value_1 + value_2 + carry
		if sum > 9 {
			sum -= 10
			carry = 1
		} else {
			carry = 0
		}
		result_current.Val = sum
		if current_1 == nil && current_2 == nil && carry == 0 {
			result_current.Next = nil
			return reverse(result)
		} else if current_1 == nil && current_2 == nil && carry != 0 {
			current_1 = &ListNode{}
		}
		result_current.Next = &ListNode{}
		result_current = result_current.Next
	}
}
