// Submission for Restore the Array From Adjacent Pairs
// Submission url: https://leetcode.com/submissions/detail/1095850051/

package submissions

func restoreArray(adjacentPairs [][]int) []int {
    graph := map[int][]int{}
    for _, pair := range adjacentPairs {
        num1, num2 := pair[0], pair[1]
        graph[num1] = append(graph[num1], num2)
        graph[num2] = append(graph[num2], num1)
    }
    var start *int
    for node, edges := range graph {
        if len(edges) == 1 {
            start = &node
        }
    }
    // [[2,1],[3,4],[3,2]]
    // 1: [2]
    // 2: [1, 3]
    // 3: [2, 4]
    // 4: [3]
    // Output: [1,2,3,4]
    length := len(adjacentPairs) + 1
    ans := make([]int, length)
    ans[0] = *start
    ans[1] = graph[*start][0]
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
