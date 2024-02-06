// Submission title: for Course Schedule II
// Submission url  : https://leetcode.com/submissions/detail/1091200613/
// Submission json : {"id": 1091200613, "status_display": "Accepted", "lang": "golang", "question_id": 210, "title_slug": "course-schedule-ii", "code": "func findOrder(numCourses int, prerequisites [][]int) []int {\n    //build the graph\n    graph := make([][]int,numCourses)\n    in_degree := make([]int,numCourses)\n    for _,v := range prerequisites{\n        graph[v[1]] = append(graph[v[1]], v[0])\n        in_degree[v[0]]++\n    }\n\n    frontier := []int{}\n    for i,v := range in_degree{\n        if v==0{\n            frontier = append(frontier,i)\n        }\n    }\n\n    result := []int{}\n    for len(frontier)!=0{\n        cur := frontier[0]\n        frontier = frontier[1:]\n        result = append(result,cur)\n        for _,v := range graph[cur]{\n            in_degree[v]--\n            if in_degree[v]==0{\n                frontier = append(frontier,v)\n            }\n        }\n    }\n\n    if len(result)==numCourses{\n        return result\n    }\n    return []int{}\n}", "title": "Course Schedule II", "url": "/submissions/detail/1091200613/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093684, "status": 10, "runtime": "9 ms", "is_pending": "Not Pending", "memory": "5.2 MB", "compare_result": "111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func findOrder(numCourses int, prerequisites [][]int) []int {
	//build the graph
	graph := make([][]int, numCourses)
	in_degree := make([]int, numCourses)
	for _, v := range prerequisites {
		graph[v[1]] = append(graph[v[1]], v[0])
		in_degree[v[0]]++
	}

	frontier := []int{}
	for i, v := range in_degree {
		if v == 0 {
			frontier = append(frontier, i)
		}
	}

	result := []int{}
	for len(frontier) != 0 {
		cur := frontier[0]
		frontier = frontier[1:]
		result = append(result, cur)
		for _, v := range graph[cur] {
			in_degree[v]--
			if in_degree[v] == 0 {
				frontier = append(frontier, v)
			}
		}
	}

	if len(result) == numCourses {
		return result
	}
	return []int{}
}
