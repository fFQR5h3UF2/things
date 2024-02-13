// Submission title: Sort List
// Submission url  : https://leetcode.com/problems/sort-list/description/
// Submission url  : https://leetcode.com/submissions/detail/1089829638/
// Submission json : {"id":1089829638,"status_display":"Accepted","lang":"golang","question_id":148,"title_slug":"sort-list","code":"\nfunc sortList(head *ListNode) *ListNode {\n\tif head == nil || head.Next == nil {\n\t\treturn head\n\t}\n\tif head.Next.Next == nil {\n\t\ta := head\n\t\tb := head.Next\n\t\tif a.Val <= b.Val {\n\t\t\ta.Next = b\n\t\t\tb.Next = nil\n\t\t\treturn a\n\t\t} else {\n\t\t\tb.Next = a\n\t\t\ta.Next = nil\n\t\t\treturn b\n\t\t}\n\t}\n\tslow := head\n\tfast := head\n\tfor fast != nil && fast.Next != nil {\n\t\tslow = slow.Next\n\t\tfast = fast.Next.Next\n\t}\n\tnextList := slow.Next\n\tslow.Next = nil\n\tlist1 := sortList(head)\n\tlist2 := sortList(nextList)\n\tdummy := &ListNode{Val: -1, Next: nil}\n\tit := dummy\n\tfor list1 != nil && list2 != nil {\n\t\tif list1.Val <= list2.Val {\n\t\t\tit.Next = list1\n\t\t\tlist1 = list1.Next\n\t\t} else {\n\t\t\tit.Next = list2\n\t\t\tlist2 = list2.Next\n\t\t}\n\t\tit = it.Next\n\t}\n\tif list1 != nil {\n\t\tit.Next = list1\n\t} else {\n\t\tit.Next = list2\n\t}\n\treturn dummy.Next\n}\n","title":"Sort List","url":"/submissions/detail/1089829638/","lang_name":"Go","time":"3 months","timestamp":1698924814,"status":10,"runtime":"53 ms","is_pending":"Not Pending","memory":"7.4 MB","compare_result":"111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func sortList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	if head.Next.Next == nil {
		a := head
		b := head.Next
		if a.Val <= b.Val {
			a.Next = b
			b.Next = nil
			return a
		} else {
			b.Next = a
			a.Next = nil
			return b
		}
	}
	slow := head
	fast := head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}
	nextList := slow.Next
	slow.Next = nil
	list1 := sortList(head)
	list2 := sortList(nextList)
	dummy := &ListNode{Val: -1, Next: nil}
	it := dummy
	for list1 != nil && list2 != nil {
		if list1.Val <= list2.Val {
			it.Next = list1
			list1 = list1.Next
		} else {
			it.Next = list2
			list2 = list2.Next
		}
		it = it.Next
	}
	if list1 != nil {
		it.Next = list1
	} else {
		it.Next = list2
	}
	return dummy.Next
}
