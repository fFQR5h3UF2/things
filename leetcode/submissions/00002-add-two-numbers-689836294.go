// Submission title: Add Two Numbers
// Submission url  : https://leetcode.com/problems/add-two-numbers/description/
// Submission url  : https://leetcode.com/submissions/detail/689836294/
// Submission json : {"id":689836294,"status_display":"Accepted","lang":"golang","question_id":2,"title_slug":"add-two-numbers","code":"\nfunc addTwoNumbers(list_1 *ListNode, list_2 *ListNode) *ListNode {\n\tcurrent_1, current_2, result := list_1, list_2, &ListNode{}\n\tvar carry int\n\tresult_current := result\n\tfor {\n\t\tvar value_1, value_2 int\n\t\tif current_1 != nil {\n\t\t\tvalue_1 = current_1.Val\n\t\t\tcurrent_1 = current_1.Next\n\t\t}\n\t\tif current_2 != nil {\n\t\t\tvalue_2 = current_2.Val\n\t\t\tcurrent_2 = current_2.Next\n\t\t}\n\t\tsum := value_1 + value_2 + carry\n\t\tif sum > 9 {\n\t\t\tsum -= 10\n\t\t\tcarry = 1\n\t\t} else {\n\t\t\tcarry = 0\n\t\t}\n\t\tresult_current.Val = sum\n\t\tif current_1 == nil && current_2 == nil && carry == 0 {\n\t\t\tresult_current.Next = nil\n\t\t\treturn result\n\t\t} else if current_1 == nil && current_2 == nil && carry != 0 {\n\t\t\tcurrent_1 = &ListNode{}\n\t\t}\n\t\tresult_current.Next = &ListNode{}\n\t\tresult_current = result_current.Next\n\t}\n}\n","title":"Add Two Numbers","url":"/submissions/detail/689836294/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651259437,"status":10,"runtime":"8 ms","is_pending":"Not Pending","memory":"4.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func addTwoNumbers(list_1 *ListNode, list_2 *ListNode) *ListNode {
	current_1, current_2, result := list_1, list_2, &ListNode{}
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
			return result
		} else if current_1 == nil && current_2 == nil && carry != 0 {
			current_1 = &ListNode{}
		}
		result_current.Next = &ListNode{}
		result_current = result_current.Next
	}
}
