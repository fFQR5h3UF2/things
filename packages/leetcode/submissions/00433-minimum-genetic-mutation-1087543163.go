// Submission title: for Minimum Genetic Mutation
// Submission url  : https://leetcode.com/submissions/detail/1087543163/
// Submission json : {"id": 1087543163, "status_display": "Accepted", "lang": "golang", "question_id": 433, "title_slug": "minimum-genetic-mutation", "code": "func minMutation(startGene string, endGene string, bank []string) int {\n    if startGene == endGene {\n        return 0\n    }\n\n    bank = append(bank, startGene)\n\n    isMut := func (gene1 string, gene2 string) bool {\n        foundDiff := false\n        for i := 0; i < len(gene1); i++ {\n            if gene1[i] == gene2[i] {\n                continue\n            }\n            if foundDiff {\n                return false\n            }\n            foundDiff = true\n        } \n        return foundDiff\n    }\n\n    graph := map[string][]string{}\n\n    for i, gene1 := range bank {\n        for _, gene2 := range bank[i+1:] {\n            if !isMut(gene1, gene2) {\n                continue\n            }\n            if _, ok := graph[gene1]; !ok {\n                graph[gene1] = []string{}\n            }\n            if _, ok := graph[gene2]; !ok {\n                graph[gene2] = []string{}\n            }\n            graph[gene1] = append(graph[gene1], gene2)\n            graph[gene2] = append(graph[gene2], gene1)\n        }\n    }\n\n    queue, ok := graph[endGene]\n    if !ok {\n        return -1\n    }\n    visited := map[string]struct{}{endGene: struct{}{}}\n    num := 1\n    for length := len(queue); length > 0; length = len(queue) {\n        for i := 0; i < length; i++ {\n            gene := queue[i]\n            if _, ok := visited[gene]; ok {\n                continue\n            }\n            if gene == startGene {\n                return num \n            }\n            visited[gene] = struct{}{}\n            queue = append(queue, graph[gene]...)\n        }\n        num += 1\n        queue = queue[length:]\n    }\n\n    return -1\n}", "title": "Minimum Genetic Mutation", "url": "/submissions/detail/1087543163/", "lang_name": "Go", "time": "3\u00a0months, 1\u00a0week", "timestamp": 1698670720, "status": 10, "runtime": "1 ms", "is_pending": "Not Pending", "memory": "2 MB", "compare_result": "111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func minMutation(startGene string, endGene string, bank []string) int {
	if startGene == endGene {
		return 0
	}

	bank = append(bank, startGene)

	isMut := func(gene1 string, gene2 string) bool {
		foundDiff := false
		for i := 0; i < len(gene1); i++ {
			if gene1[i] == gene2[i] {
				continue
			}
			if foundDiff {
				return false
			}
			foundDiff = true
		}
		return foundDiff
	}

	graph := map[string][]string{}

	for i, gene1 := range bank {
		for _, gene2 := range bank[i+1:] {
			if !isMut(gene1, gene2) {
				continue
			}
			if _, ok := graph[gene1]; !ok {
				graph[gene1] = []string{}
			}
			if _, ok := graph[gene2]; !ok {
				graph[gene2] = []string{}
			}
			graph[gene1] = append(graph[gene1], gene2)
			graph[gene2] = append(graph[gene2], gene1)
		}
	}

	queue, ok := graph[endGene]
	if !ok {
		return -1
	}
	visited := map[string]struct{}{endGene: struct{}{}}
	num := 1
	for length := len(queue); length > 0; length = len(queue) {
		for i := 0; i < length; i++ {
			gene := queue[i]
			if _, ok := visited[gene]; ok {
				continue
			}
			if gene == startGene {
				return num
			}
			visited[gene] = struct{}{}
			queue = append(queue, graph[gene]...)
		}
		num += 1
		queue = queue[length:]
	}

	return -1
}
