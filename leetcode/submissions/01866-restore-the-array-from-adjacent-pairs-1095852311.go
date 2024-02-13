// Submission title: Restore the Array From Adjacent Pairs
// Submission url  : https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
// Submission url  : https://leetcode.com/submissions/detail/1095852311/
// Submission json : {"id":1095852311,"status_display":"Accepted","lang":"golang","question_id":1866,"title_slug":"restore-the-array-from-adjacent-pairs","code":"func restoreArray(adjacentPairs [][]int) []int {\n    // [[2,1],[3,4],[3,2]]\n    // 1: [2]\n    // 2: [1, 3]\n    // 3: [2, 4]\n    // 4: [3]\n    // Output: [1,2,3,4]\n    graph := map[int][]int{}\n    for _, pair := range adjacentPairs {\n        num1, num2 := pair[0], pair[1]\n        graph[num1] = append(graph[num1], num2)\n        graph[num2] = append(graph[num2], num1)\n    }\n    length := len(adjacentPairs) + 1\n    ans := make([]int, length)\n    for node, edges := range graph {\n        if len(edges) == 1 {\n            ans[0], ans[1] = node, edges[0]\n            break\n        }\n    }\n    for i := 2; i < length; i++ {\n        cur, prev := ans[i-1], ans[i-2]\n        for _, target := range graph[cur] {\n            if target != prev {\n                ans[i] = target\n            }\n        }\n    }\n    return ans\n}","title":"Restore the Array From Adjacent Pairs","url":"/submissions/detail/1095852311/","lang_name":"Go","time":"2 months, 3 weeks","timestamp":1699611896,"status":10,"runtime":"184 ms","is_pending":"Not Pending","memory":"34.6 MB","compare_result":"1111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func restoreArray(adjacentPairs [][]int) []int {
	// [[2,1],[3,4],[3,2]]
	// 1: [2]
	// 2: [1, 3]
	// 3: [2, 4]
	// 4: [3]
	// Output: [1,2,3,4]
	graph := map[int][]int{}
	for _, pair := range adjacentPairs {
		num1, num2 := pair[0], pair[1]
		graph[num1] = append(graph[num1], num2)
		graph[num2] = append(graph[num2], num1)
	}
	length := len(adjacentPairs) + 1
	ans := make([]int, length)
	for node, edges := range graph {
		if len(edges) == 1 {
			ans[0], ans[1] = node, edges[0]
			break
		}
	}
	for i := 2; i < length; i++ {
		cur, prev := ans[i-1], ans[i-2]
		for _, target := range graph[cur] {
			if target != prev {
				ans[i] = target
			}
		}
	}
	return ans
}
