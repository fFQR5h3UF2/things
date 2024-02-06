// Submission title: for Find Mode in Binary Search Tree
// Submission url  : https://leetcode.com/submissions/detail/1089001471/
// Submission json : {"id": 1089001471, "status_display": "Accepted", "lang": "golang", "question_id": 501, "title_slug": "find-mode-in-binary-search-tree", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\nfunc findMode(root *TreeNode) []int {\n    if root == nil {\n        return []int{}\n    }\n    counter := map[int]int{}\n    dfs(root, counter)\n    maxCount, answer := 0, []int{}\n    for key, count := range counter {\n        if count < maxCount {\n            continue\n        }\n        if count > maxCount {\n            answer = answer[:0]\n            maxCount = count\n        }\n        answer = append(answer, key)\n    }\n    return answer\n}\n\nfunc dfs(root *TreeNode, counter map[int]int) {\n    if root == nil {\n        return\n    }\n    if _, ok := counter[root.Val]; ok {\n        counter[root.Val] += 1\n    } else {\n        counter[root.Val] = 1\n    }\n    dfs(root.Left, counter)\n    dfs(root.Right, counter)\n}", "title": "Find Mode in Binary Search Tree", "url": "/submissions/detail/1089001471/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1698830896, "status": 10, "runtime": "12 ms", "is_pending": "Not Pending", "memory": "6.6 MB", "compare_result": "11111111111111111111111", "has_notes": true, "flag_type": 1}

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
	dfs(root, counter)
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

func dfs(root *TreeNode, counter map[int]int) {
	if root == nil {
		return
	}
	if _, ok := counter[root.Val]; ok {
		counter[root.Val] += 1
	} else {
		counter[root.Val] = 1
	}
	dfs(root.Left, counter)
	dfs(root.Right, counter)
}
