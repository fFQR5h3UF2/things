// Submission title: Merge Two Sorted Lists
// Submission url  : https://leetcode.com/problems/merge-two-sorted-lists/description/
// Submission url  : https://leetcode.com/submissions/detail/690739883/
// Submission json : {"id":690739883,"status_display":"Accepted","lang":"golang","question_id":21,"title_slug":"merge-two-sorted-lists","code":"func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {\n\t// ensure both lists are valid\n\tswitch {\n\tcase list1 == nil && list2 == nil:\n\t\treturn nil\n\tcase list1 == nil && list2 != nil:\n\t\treturn list2\n\tcase list1 != nil && list2 == nil:\n\t\treturn list1\n\t}\n\tvar root *ListNode\n\tif list1.Val < list2.Val {\n\t\troot = &ListNode{list1.Val, nil}\n\t\tlist1 = list1.Next\n\t} else {\n\t\troot = &ListNode{list2.Val, nil}\n\t\tlist2 = list2.Next\n\t}\n\tcurrent := &root\n\tfor {\n\t\tswitch {\n\t\tcase list1 == nil && list2 == nil:\n\t\t\treturn root\n\t\tcase list1 != nil && list2 != nil && list1.Val <= list2.Val:\n\t\t\tfallthrough\n\t\tcase list1 != nil && list2 == nil:\n\t\t\tfmt.Println(\"1\", list1.Val)\n\t\t\tupdateResult(&current, &list1)\n\t\tcase list1 != nil && list2 != nil && list1.Val > list2.Val:\n\t\t\tfallthrough\n\t\tcase list1 == nil && list2 != nil:\n\t\t\tfmt.Println(\"2\", list2.Val)\n\t\t\tupdateResult(&current, &list2)\n\t\t}\n\t}\n}\nfunc updateResult(current ***ListNode, node **ListNode) {\n\t// modify the current result node\n\t(**current).Next = &ListNode{(*node).Val, nil}\n\t// move the current pointer\n\t*current = &(**current).Next\n\t// there is no next node -> nill it\n\t// there is next -> move it\n\tif (*node).Next == nil {\n\t\t*node = nil\n\t} else {\n\t\t*node = (*node).Next\n\t}\n}\n","title":"Merge Two Sorted Lists","url":"/submissions/detail/690739883/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651385208,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"2.8 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	// ensure both lists are valid
	switch {
	case list1 == nil && list2 == nil:
		return nil
	case list1 == nil && list2 != nil:
		return list2
	case list1 != nil && list2 == nil:
		return list1
	}
	var root *ListNode
	if list1.Val < list2.Val {
		root = &ListNode{list1.Val, nil}
		list1 = list1.Next
	} else {
		root = &ListNode{list2.Val, nil}
		list2 = list2.Next
	}
	current := &root
	for {
		switch {
		case list1 == nil && list2 == nil:
			return root
		case list1 != nil && list2 != nil && list1.Val <= list2.Val:
			fallthrough
		case list1 != nil && list2 == nil:
			fmt.Println("1", list1.Val)
			updateResult(&current, &list1)
		case list1 != nil && list2 != nil && list1.Val > list2.Val:
			fallthrough
		case list1 == nil && list2 != nil:
			fmt.Println("2", list2.Val)
			updateResult(&current, &list2)
		}
	}
}
func updateResult(current ***ListNode, node **ListNode) {
	// modify the current result node
	(**current).Next = &ListNode{(*node).Val, nil}
	// move the current pointer
	*current = &(**current).Next
	// there is no next node -> nill it
	// there is next -> move it
	if (*node).Next == nil {
		*node = nil
	} else {
		*node = (*node).Next
	}
}
