// Submission title: Word Search II
// Submission url  : https://leetcode.com/problems/word-search-ii/description/
// Submission url  : https://leetcode.com/submissions/detail/1091201217/
// Submission json : {"id":1091201217,"status_display":"Accepted","lang":"golang","question_id":212,"title_slug":"word-search-ii","code":"type Node struct {\n\tchildren [26]*Node\n\tword     string\n}\n\nfunc (n *Node) Insert(word string) {\n\tcur := n\n\tfor _, c := range word {\n\t\tidx := c - 'a'\n\t\tif cur.children[idx] == nil {\n\t\t\tcur.children[idx] = &Node{}\n\t\t}\n\t\tcur = cur.children[idx]\n\t}\n\tcur.word = word\n}\n\nfunc (n *Node) IsEmpty() bool {\n\tfor _, child := range n.children {\n\t\tif child != nil {\n\t\t\treturn false\n\t\t}\n\t}\n\treturn true\n}\n\nfunc (n *Node) Remove(word string) bool {\n\tif len(word) == 0 {\n\t\tn.word = \"\"\n\t\treturn n.IsEmpty()\n\t}\n\tchild := n.children[word[0]-'a']\n\tif child.Remove(word[1:]) {\n\t\tn.children[word[0]-'a'] = nil\n\t\treturn n.IsEmpty()\n\t}\n\treturn false\n}\n\nfunc dfs(board [][]byte, r, c int, root, cur *Node, res *[]string) {\n\trc := board[r][c]\n\tboard[r][c] = 0\n    \n\tif cur.word != \"\" {\n\t\t*res = append(*res, cur.word)\n\t\troot.Remove(cur.word)\n\t}\n\tds := [5]int{0, 1, 0, -1, 0}\n\tfor i := 0; i < len(ds)-1; i++ {\n\t\tdr, dc := r+ds[i], c+ds[i+1]\n\t\tif dr < 0 || dr >= len(board) || dc < 0 || dc >= len(board[0]) {\n\t\t\tcontinue\n\t\t}\n\t\tb := board[dr][dc]\n\t\tif b == 0 || cur.children[b-'a'] == nil {\n\t\t\tcontinue\n\t\t}\n\t\tdfs(board, dr, dc, root, cur.children[b-'a'], res)\n\t}\n\tboard[r][c] = rc\n}\n\nfunc findWords(board [][]byte, words []string) []string {\n\tm, n := len(board), len(board[0])\n\tres, trie, has := []string{}, &Node{}, map[string]bool{}\n\n\tfor r := 0; r < m; r++ {\n\t\tfor c := 0; c < n-1; c++ {\n\t\t\tp := string(board[r][c]) + string(board[r][c+1])\n\t\t\thas[p] = true\n\t\t}\n\t}\n\tfor r := 0; r < m-1; r++ {\n\t\tfor c := 0; c < n; c++ {\n\t\t\tp := string(board[r][c]) + string(board[r+1][c])\n\t\t\thas[p] = true\n\t\t}\n\t}\n\tfor _, word := range words {\n\t\tvalid := true\n\t\tfor i := 0; i < len(word)-1; i++ {\n\t\t\ta, b := string(word[i]), string(word[i+1])\n\t\t\tif !has[a+b] && !has[b+a] {\n\t\t\t\tvalid = false\n\t\t\t\tbreak\n\t\t\t}\n\t\t}\n\t\tif valid {\n\t\t\ttrie.Insert(word)\n\t\t}\n\t}\n\tfor r := 0; r < m; r++ {\n\t\tfor c := 0; c < n; c++ {\n\t\t\tb := board[r][c]\n\t\t\tif trie.children[b-'a'] != nil {\n\t\t\t\tdfs(board, r, c, trie, trie.children[b-'a'], &res)\n\t\t\t}\n\t\t}\n\t}\n\treturn res\n}","title":"Word Search II","url":"/submissions/detail/1091201217/","lang_name":"Go","time":"3 months","timestamp":1699093756,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"2.8 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

type Node struct {
	children [26]*Node
	word     string
}

func (n *Node) Insert(word string) {
	cur := n
	for _, c := range word {
		idx := c - 'a'
		if cur.children[idx] == nil {
			cur.children[idx] = &Node{}
		}
		cur = cur.children[idx]
	}
	cur.word = word
}

func (n *Node) IsEmpty() bool {
	for _, child := range n.children {
		if child != nil {
			return false
		}
	}
	return true
}

func (n *Node) Remove(word string) bool {
	if len(word) == 0 {
		n.word = ""
		return n.IsEmpty()
	}
	child := n.children[word[0]-'a']
	if child.Remove(word[1:]) {
		n.children[word[0]-'a'] = nil
		return n.IsEmpty()
	}
	return false
}

func dfs(board [][]byte, r, c int, root, cur *Node, res *[]string) {
	rc := board[r][c]
	board[r][c] = 0

	if cur.word != "" {
		*res = append(*res, cur.word)
		root.Remove(cur.word)
	}
	ds := [5]int{0, 1, 0, -1, 0}
	for i := 0; i < len(ds)-1; i++ {
		dr, dc := r+ds[i], c+ds[i+1]
		if dr < 0 || dr >= len(board) || dc < 0 || dc >= len(board[0]) {
			continue
		}
		b := board[dr][dc]
		if b == 0 || cur.children[b-'a'] == nil {
			continue
		}
		dfs(board, dr, dc, root, cur.children[b-'a'], res)
	}
	board[r][c] = rc
}

func findWords(board [][]byte, words []string) []string {
	m, n := len(board), len(board[0])
	res, trie, has := []string{}, &Node{}, map[string]bool{}

	for r := 0; r < m; r++ {
		for c := 0; c < n-1; c++ {
			p := string(board[r][c]) + string(board[r][c+1])
			has[p] = true
		}
	}
	for r := 0; r < m-1; r++ {
		for c := 0; c < n; c++ {
			p := string(board[r][c]) + string(board[r+1][c])
			has[p] = true
		}
	}
	for _, word := range words {
		valid := true
		for i := 0; i < len(word)-1; i++ {
			a, b := string(word[i]), string(word[i+1])
			if !has[a+b] && !has[b+a] {
				valid = false
				break
			}
		}
		if valid {
			trie.Insert(word)
		}
	}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			b := board[r][c]
			if trie.children[b-'a'] != nil {
				dfs(board, r, c, trie, trie.children[b-'a'], &res)
			}
		}
	}
	return res
}
