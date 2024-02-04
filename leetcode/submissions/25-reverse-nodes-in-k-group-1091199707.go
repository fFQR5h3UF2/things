// Submission for Reverse Nodes in k-Group
// Submission url: https://leetcode.com/submissions/detail/1091199707/

package submissions

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

/* Recursive Solution */

func reverseKGroup(head *ListNode, k int) *ListNode {
    l := length(head)
    return reverse(head, l, k)
}

func reverse(node *ListNode, l, k int) *ListNode {
    if l < k {
        return node
    }

    var prev, next *ListNode
    curr := node
    for i := 0; i < k; i++ {
        next = curr.Next
        curr.Next = prev
        prev = curr
        curr = next
    }

    node.Next = reverse(next, l-k, k)
    return prev
}

func length(head *ListNode) int {
    count := 0

    for head != nil {
        head = head.Next
        count++
    }
    return count
}

/* Iterative Solution */

func reverseKGroup(head *ListNode, k int) *ListNode {
    if head == nil || k == 1 {
        return head
    }

    l := length(head)
    preHead := &ListNode{Next: head}

    prev := preHead
    for l >= k {
        curr := prev.Next
        for i := 1; i < k; i++ {
            next := curr.Next
            curr.Next = next.Next
            next.Next = prev.Next
            prev.Next = next
        }
        prev = curr
        l -= k
    }

    return preHead.Next
}

func length(head *ListNode) int {
    count := 0

    for head != nil {
        head = head.Next
        count++
    }
    return count
}
