// Submission title: Reverse Nodes in k-Group
// Submission url  : https://leetcode.com/problems/reverse-nodes-in-k-group/description/
// Submission url  : https://leetcode.com/submissions/detail/1091200011/
// Submission json : {"id":1091200011,"status_display":"Accepted","lang":"golang","question_id":25,"title_slug":"reverse-nodes-in-k-group","code":"func reverseKGroup(head *ListNode, k int) *ListNode {\n\tnode, cnt := head, 0\n\tfor cnt < k {\n\t\tif node == nil {\n\t\t\treturn head\n\t\t}\n\t\tnode = node.Next\n\t\tcnt++\n\t}\n\n\tprev := reverseKGroup(node, k)\n\tfor cnt > 0 {\n\t\tnext := head.Next\n\t\thead.Next = prev\n\t\tprev = head\n\t\thead = next\n\t\tcnt--\n\t}\n\n\treturn prev\n}","title":"Reverse Nodes in k-Group","url":"/submissions/detail/1091200011/","lang_name":"Go","time":"3 months","timestamp":1699093602,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"3.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

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
