// Submission title: Word Ladder
// Submission url  : https://leetcode.com/problems/word-ladder/description/
// Submission url  : https://leetcode.com/submissions/detail/1091201004/
// Submission json : {"id":1091201004,"status_display":"Accepted","lang":"golang","question_id":127,"title_slug":"word-ladder","code":"func ladderLength(beginWord string, endWord string, wordList []string) int {\n    \n    set := make(map[string]struct{}, len(wordList))\n    \n    present := false\n    \n    for _, v := range wordList {\n        if endWord == v {\n            present = true\n        } \n        \n        set[v] = struct{}{} \n    }\n    \n    if !present {\n        return 0\n    }\n    \n    set[beginWord] = struct{}{}\n    q := []string{beginWord}\n    \n    depth := 1\n    breadth := 0\n    \n    breadth = len(q)\n    \n    for ;breadth > 0; {\n        s := q[0]\n        \n        if s == endWord {\n            return depth\n        }\n        \n        for i:='a'; i <= 'z'; i += 1 {\n                        \n            for j := 0; j<len(s); j++ {\n \n                if rune(s[j]) != i {\n                    \n                    temp := s[:j] + string(i) + s[j+1:]\n                    if _, ok := set[temp]; !ok {\n                        continue\n                    }\n                    \n                    q = append(q, temp)\n                    delete(set, s)\n                }\n            }\n        }\n        \n        q = q[1:]\n        \n        breadth -= 1\n        if breadth == 0 {\n            breadth = len(q)\n            depth += 1\n        }\n    }\n    \n    return 0 \n}","title":"Word Ladder","url":"/submissions/detail/1091201004/","lang_name":"Go","time":"3 months","timestamp":1699093730,"status":10,"runtime":"2746 ms","is_pending":"Not Pending","memory":"8 MB","compare_result":"111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func ladderLength(beginWord string, endWord string, wordList []string) int {

	set := make(map[string]struct{}, len(wordList))

	present := false

	for _, v := range wordList {
		if endWord == v {
			present = true
		}

		set[v] = struct{}{}
	}

	if !present {
		return 0
	}

	set[beginWord] = struct{}{}
	q := []string{beginWord}

	depth := 1
	breadth := 0

	breadth = len(q)

	for breadth > 0 {
		s := q[0]

		if s == endWord {
			return depth
		}

		for i := 'a'; i <= 'z'; i += 1 {

			for j := 0; j < len(s); j++ {

				if rune(s[j]) != i {

					temp := s[:j] + string(i) + s[j+1:]
					if _, ok := set[temp]; !ok {
						continue
					}

					q = append(q, temp)
					delete(set, s)
				}
			}
		}

		q = q[1:]

		breadth -= 1
		if breadth == 0 {
			breadth = len(q)
			depth += 1
		}
	}

	return 0
}
