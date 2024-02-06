// Submission title: for Kth Smallest Element in a BST
// Submission url  : https://leetcode.com/submissions/detail/1090575563/
// Submission json : {"id": 1090575563, "status_display": "Accepted", "lang": "golang", "question_id": 230, "title_slug": "kth-smallest-element-in-a-bst", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc kthSmallest(root *TreeNode, k int) int {\n    heap := binaryheap.NewWithIntComparator()\n    queue := []*TreeNode{root}\n\n    for length := len(queue); length > 0; length = len(queue) {\n        for i := 0; i < length; i++ {\n            node := queue[i]\n            if node == nil {\n                continue\n            }\n            heap.Push(node.Val)\n            queue = append(queue, node.Left, node.Right)\n        }\n        queue = queue[length:]\n    }\n    var answer any\n    for i := 0; i < k; i++ {\n        answer, _ = heap.Pop()\n    }\n    return answer.(int)\n}\n", "title": "Kth Smallest Element in a BST", "url": "/submissions/detail/1090575563/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699014026, "status": 10, "runtime": "12 ms", "is_pending": "Not Pending", "memory": "6.8 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func kthSmallest(root *TreeNode, k int) int {
	heap := binaryheap.NewWithIntComparator()
	queue := []*TreeNode{root}

	for length := len(queue); length > 0; length = len(queue) {
		for i := 0; i < length; i++ {
			node := queue[i]
			if node == nil {
				continue
			}
			heap.Push(node.Val)
			queue = append(queue, node.Left, node.Right)
		}
		queue = queue[length:]
	}
	var answer any
	for i := 0; i < k; i++ {
		answer, _ = heap.Pop()
	}
	return answer.(int)
}
