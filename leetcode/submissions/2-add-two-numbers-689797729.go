// Submission for Add Two Numbers
// Submission url: https://leetcode.com/submissions/detail/689797729/

package submissions

import "fmt"

func to_list(number int) *ListNode {
	remainder := number / 10
	result := &ListNode{number % 10, nil}
	current := result
	for {
		if remainder == 0 {
			return result
		}
		current.Next = &ListNode{remainder % 10, nil}
		current = current.Next
        remainder /= 10
	}
}



func from_list(list *ListNode) (result int) {
	current := list
	for order := 1; ; order *= 10 {
		value := current.Val
		if value == 0 {
			value = 1
		}
		result += value * order
		if current.Next == nil {
			return
		}
		current = current.Next
	}
}

func addTwoNumbers(list_1 *ListNode, list_2 *ListNode) *ListNode {

fmt.Println(list_1, from_list(list_1))
    fmt.Println(list_2, from_list(list_2))
    return to_list(from_list(list_1) + from_list(list_2))
}
