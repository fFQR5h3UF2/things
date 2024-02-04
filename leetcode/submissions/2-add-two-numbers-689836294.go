// Submission for Add Two Numbers
// Submission url: https://leetcode.com/submissions/detail/689836294/

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
