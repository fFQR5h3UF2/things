// Submission title: for IPO
// Submission url  : https://leetcode.com/submissions/detail/1091201914/
// Submission json : {"id": 1091201914, "status_display": "Accepted", "lang": "golang", "question_id": 502, "title_slug": "ipo", "code": "type Project struct {\n    profit, capital int\n}\n\ntype IntHeap []int\nfunc (h IntHeap) Len() int           { return len(h) }\nfunc (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }\nfunc (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }\nfunc (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }\nfunc (h *IntHeap) Pop() interface{} {\n\told := *h\n\tn := len(old)\n\tx := old[n-1]\n\t*h = old[0 : n-1]\n\treturn x\n}\n\nfunc findMaximizedCapital(k int, w int, profits []int, capital []int) int {\n    n := len(profits)\n    projects := make([]Project, n)\n    for i := range profits {\n        projects[i] = Project{profits[i], capital[i]}\n    }\n    sort.Slice(projects, func (i, j int) bool {\n        return projects[i].capital < projects[j].capital\n    })\n    \n    q := &IntHeap{}\n    heap.Init(q)\n\n    ptr := 0\n    for i := 0; i < k; i++ {\n        for ptr < n && projects[ptr].capital <= w {\n            heap.Push(q, projects[ptr].profit)\n            ptr++\n        }\n        if q.Len() == 0 {\n            break\n        }\n        w += heap.Pop(q).(int)\n    }\n    return w\n}", "title": "IPO", "url": "/submissions/detail/1091201914/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093845, "status": 10, "runtime": "155 ms", "is_pending": "Not Pending", "memory": "10.8 MB", "compare_result": "11111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

type Project struct {
	profit, capital int
}

type IntHeap []int

func (h IntHeap) Len() int            { return len(h) }
func (h IntHeap) Less(i, j int) bool  { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func findMaximizedCapital(k int, w int, profits []int, capital []int) int {
	n := len(profits)
	projects := make([]Project, n)
	for i := range profits {
		projects[i] = Project{profits[i], capital[i]}
	}
	sort.Slice(projects, func(i, j int) bool {
		return projects[i].capital < projects[j].capital
	})

	q := &IntHeap{}
	heap.Init(q)

	ptr := 0
	for i := 0; i < k; i++ {
		for ptr < n && projects[ptr].capital <= w {
			heap.Push(q, projects[ptr].profit)
			ptr++
		}
		if q.Len() == 0 {
			break
		}
		w += heap.Pop(q).(int)
	}
	return w
}
