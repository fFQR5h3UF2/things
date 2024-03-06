// Submission title: Linked List Cycle
// Submission url  : https://leetcode.com/problems/linked-list-cycle/description/
// Submission url  : https://leetcode.com/submissions/detail/1195713652/"
package submissions

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	nodes := map[*ListNode]struct{}{}
	for head != nil {
		if _, ok := nodes[head]; ok {
			return true
		}
		nodes[head] = struct{}{}
		head = head.Next
	}
	return false
}
