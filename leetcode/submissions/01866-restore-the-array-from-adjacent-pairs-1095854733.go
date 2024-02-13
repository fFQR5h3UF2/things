// Submission title: Restore the Array From Adjacent Pairs
// Submission url  : https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
// Submission url  : https://leetcode.com/submissions/detail/1095854733/
// Submission json : {"id":1095854733,"status_display":"Accepted","lang":"golang","question_id":1866,"title_slug":"restore-the-array-from-adjacent-pairs","code":"func restoreArray(adjacentPairs [][]int) []int {\n    // [[2,1],[3,4],[3,2]]\n    // 1: [2]\n    // 2: [1, 3]\n    // 3: [2, 4]\n    // 4: [3]\n    // Output: [1,2,3,4]\n    graph := map[int][]int{}\n    length := len(adjacentPairs) + 1\n    ans := make([]int, length)\n    for _, pair := range adjacentPairs {\n        num1, num2 := pair[0], pair[1]\n        graph[num1] = append(graph[num1], num2)\n        graph[num2] = append(graph[num2], num1)\n    }\n    for node, edges := range graph {\n        if len(edges) == 1 {\n            ans[0], ans[1] = node, edges[0]\n            break\n        }\n    }\n    cur, prev := ans[1], ans[0]\n    for i := 2; i < length; i++ {\n        for _, target := range graph[cur] {\n            if target != prev {\n                ans[i] = target\n                cur, prev = target, cur\n                break\n            }\n        }\n    }\n    return ans\n}","title":"Restore the Array From Adjacent Pairs","url":"/submissions/detail/1095854733/","lang_name":"Go","time":"2 months, 3 weeks","timestamp":1699612237,"status":10,"runtime":"158 ms","is_pending":"Not Pending","memory":"31.3 MB","compare_result":"1111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func restoreArray(adjacentPairs [][]int) []int {
	// [[2,1],[3,4],[3,2]]
	// 1: [2]
	// 2: [1, 3]
	// 3: [2, 4]
	// 4: [3]
	// Output: [1,2,3,4]
	graph := map[int][]int{}
	length := len(adjacentPairs) + 1
	ans := make([]int, length)
	for _, pair := range adjacentPairs {
		num1, num2 := pair[0], pair[1]
		graph[num1] = append(graph[num1], num2)
		graph[num2] = append(graph[num2], num1)
	}
	for node, edges := range graph {
		if len(edges) == 1 {
			ans[0], ans[1] = node, edges[0]
			break
		}
	}
	cur, prev := ans[1], ans[0]
	for i := 2; i < length; i++ {
		for _, target := range graph[cur] {
			if target != prev {
				ans[i] = target
				cur, prev = target, cur
				break
			}
		}
	}
	return ans
}
