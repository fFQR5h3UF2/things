// Submission title: for Minimum Window Substring
// Submission url  : https://leetcode.com/submissions/detail/1091199352/
// Submission json : {"id": 1091199352, "status_display": "Accepted", "lang": "golang", "question_id": 76, "title_slug": "minimum-window-substring", "code": "func minWindow(s string, t string) string {\n    m := len(s)\n    n := len(t)\n    \n    if m == 0 || n == 0 || m < n {\n        return \"\"\n    }\n\n    dict := make(map[byte]int)\n    for i := 0; i < n; i++ {\n        dict[t[i]]++\n    }\n    \n    // required unique chars\n    required := len(dict)\n    actual := 0\n    window := make(map[byte]int)\n    minSize := math.MaxInt64\n    start := 0\n    left, right := 0, 0\n    \n    for end := 0; end < m; end++ {\n        c := s[end]\n        window[c]++\n        \n        if value, ok := dict[c]; ok {\n            if value == window[c] {\n                actual++\n            }\n        }\n        \n        for start <= end && actual == required {\n            size := end-start+1\n            if size < minSize {\n                minSize = size\n                left = start\n                right = end\n            }\n            \n            rc := s[start]\n            window[rc]--\n            if value, ok := dict[rc]; ok {\n                if value > window[rc] {\n                    actual--\n                }\n            }\n            start++\n        }\n    }\n    \n    if minSize == math.MaxInt64 {\n        return \"\"\n    }\n    return s[left:right+1]\n}", "title": "Minimum Window Substring", "url": "/submissions/detail/1091199352/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699093514, "status": 10, "runtime": "19 ms", "is_pending": "Not Pending", "memory": "3.1 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func minWindow(s string, t string) string {
	m := len(s)
	n := len(t)

	if m == 0 || n == 0 || m < n {
		return ""
	}

	dict := make(map[byte]int)
	for i := 0; i < n; i++ {
		dict[t[i]]++
	}

	// required unique chars
	required := len(dict)
	actual := 0
	window := make(map[byte]int)
	minSize := math.MaxInt64
	start := 0
	left, right := 0, 0

	for end := 0; end < m; end++ {
		c := s[end]
		window[c]++

		if value, ok := dict[c]; ok {
			if value == window[c] {
				actual++
			}
		}

		for start <= end && actual == required {
			size := end - start + 1
			if size < minSize {
				minSize = size
				left = start
				right = end
			}

			rc := s[start]
			window[rc]--
			if value, ok := dict[rc]; ok {
				if value > window[rc] {
					actual--
				}
			}
			start++
		}
	}

	if minSize == math.MaxInt64 {
		return ""
	}
	return s[left : right+1]
}
