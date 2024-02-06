// Submission title: for Find Mode in Binary Search Tree
// Submission url  : https://leetcode.com/submissions/detail/1089003627/
// Submission json : {"id": 1089003627, "status_display": "Accepted", "lang": "golang", "question_id": 501, "title_slug": "find-mode-in-binary-search-tree", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc findMode(root *TreeNode) []int {\n    if root == nil {\n        return []int{}\n    }\n    counter := map[int]int{}\n    queue := []*TreeNode{root}\n    for length := len(queue); length > 0; length = len(queue) {\n        for i := 0; i < length; i++ {\n            node := queue[i]\n            if node == nil {\n                continue\n            }\n            if val, ok := counter[node.Val]; ok {\n                counter[node.Val] = val + 1\n            } else {\n                counter[node.Val] = 1\n            }\n            queue = append(queue, node.Left, node.Right)\n        }\n        queue = queue[length:]\n    }\n    maxCount, answer := 0, []int{}\n    for key, count := range counter {\n        if count < maxCount {\n            continue\n        }\n        if count > maxCount {\n            answer = answer[:0]\n            maxCount = count\n        }\n        answer = append(answer, key)\n    }\n    return answer\n}", "title": "Find Mode in Binary Search Tree", "url": "/submissions/detail/1089003627/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698831146, "status": 10, "runtime": "9 ms", "is_pending": "Not Pending", "memory": "6.6 MB", "compare_result": "11111111111111111111111", "has_notes": true, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findMode(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	counter := map[int]int{}
	queue := []*TreeNode{root}
	for length := len(queue); length > 0; length = len(queue) {
		for i := 0; i < length; i++ {
			node := queue[i]
			if node == nil {
				continue
			}
			if val, ok := counter[node.Val]; ok {
				counter[node.Val] = val + 1
			} else {
				counter[node.Val] = 1
			}
			queue = append(queue, node.Left, node.Right)
		}
		queue = queue[length:]
	}
	maxCount, answer := 0, []int{}
	for key, count := range counter {
		if count < maxCount {
			continue
		}
		if count > maxCount {
			answer = answer[:0]
			maxCount = count
		}
		answer = append(answer, key)
	}
	return answer
}
