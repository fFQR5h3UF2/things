# Submission for 'Reverse Nodes in k-Group'
# Submission url: https://leetcode.com/submissions/detail/1091200011/

func reverseKGroup(head *ListNode, k int) *ListNode {
	node, cnt := head, 0
	for cnt < k {
		if node == nil {
			return head
		}
		node = node.Next
		cnt++
	}

	prev := reverseKGroup(node, k)
	for cnt > 0 {
		next := head.Next
		head.Next = prev
		prev = head
		head = next
		cnt--
	}

	return prev
}
