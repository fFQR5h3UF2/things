// Submission title: for Merge k Sorted Lists
// Submission url  : https://leetcode.com/submissions/detail/1091201621/
// Submission json : {"id": 1091201621, "status_display": "Accepted", "lang": "golang", "question_id": 23, "title_slug": "merge-k-sorted-lists", "code": "/**\n * Definition for singly-linked list.\n * type ListNode struct {\n *     Val int\n *     Next *ListNode\n * }\n */\nfunc mergeKLists(lists []*ListNode) *ListNode {\n    n:=len(lists)\n    if n==0{\n        return nil\n    }\n    curr:=lists[0]\n    if n==1{\n        return curr\n    }\n    for i:=1;i<n;i++{\n        curr=mergeList(curr,lists[i])\n    }\n    return curr\n}\n\nfunc mergeList(l1,l2 *ListNode) *ListNode {\n    head:=&ListNode{}\n    curr:=head\n    for l1!=nil && l2!=nil{\n        if l1.Val<l2.Val{\n            curr.Next=l1\n            l1=l1.Next\n            curr=curr.Next\n        }else{\n            curr.Next=l2\n            l2=l2.Next\n            curr=curr.Next\n        }\n    }\n    if l1 != nil {\n        curr.Next = l1\n    } else if l2 != nil {\n        curr.Next = l2\n    }\n    return head.Next\n}", "title": "Merge k Sorted Lists", "url": "/submissions/detail/1091201621/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093807, "status": 10, "runtime": "81 ms", "is_pending": "Not Pending", "memory": "5 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
	n := len(lists)
	if n == 0 {
		return nil
	}
	curr := lists[0]
	if n == 1 {
		return curr
	}
	for i := 1; i < n; i++ {
		curr = mergeList(curr, lists[i])
	}
	return curr
}

func mergeList(l1, l2 *ListNode) *ListNode {
	head := &ListNode{}
	curr := head
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			curr.Next = l1
			l1 = l1.Next
			curr = curr.Next
		} else {
			curr.Next = l2
			l2 = l2.Next
			curr = curr.Next
		}
	}
	if l1 != nil {
		curr.Next = l1
	} else if l2 != nil {
		curr.Next = l2
	}
	return head.Next
}
