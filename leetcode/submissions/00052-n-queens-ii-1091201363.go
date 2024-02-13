// Submission title: N-Queens II
// Submission url  : https://leetcode.com/problems/n-queens-ii/description/
// Submission url  : https://leetcode.com/submissions/detail/1091201363/
// Submission json : {"id":1091201363,"status_display":"Accepted","lang":"golang","question_id":52,"title_slug":"n-queens-ii","code":"func totalNQueens(n int) int {\n    sCol:=make([]bool,n)\n    sD1:=make([]bool,2*n)\n    sD2:=make([]bool,2*n)\n    return helper(0,n,sCol,sD1,sD2)\n}\nfunc helper(r,n int,sCol,sD1,sD2 []bool) int{\n    if r==n{\n        return 1\n    }\n    res:=0\n    for i:=0; i < n; i++ {\n        if !sCol[i] && !sD1[i+r] && !sD2[(r-i)+n]{\n          // board[r][i]=true\n            sCol[i]=true\n            sD1[i+r]=true\n            sD2[(r-i)+n]=true\n            res=res+helper(r+1,n,sCol,sD1,sD2)\n          //  board[r][i]=false\n            sCol[i]=false\n            sD1[i+r]=false\n            sD2[(r-i)+n]=false\n        }\n    }\n    return res\n}","title":"N-Queens II","url":"/submissions/detail/1091201363/","lang_name":"Go","time":"3 months","timestamp":1699093774,"status":10,"runtime":"1 ms","is_pending":"Not Pending","memory":"2 MB","compare_result":"111111111","has_notes":false,"flag_type":1}
package submissions

func totalNQueens(n int) int {
	sCol := make([]bool, n)
	sD1 := make([]bool, 2*n)
	sD2 := make([]bool, 2*n)
	return helper(0, n, sCol, sD1, sD2)
}
func helper(r, n int, sCol, sD1, sD2 []bool) int {
	if r == n {
		return 1
	}
	res := 0
	for i := 0; i < n; i++ {
		if !sCol[i] && !sD1[i+r] && !sD2[(r-i)+n] {
			// board[r][i]=true
			sCol[i] = true
			sD1[i+r] = true
			sD2[(r-i)+n] = true
			res = res + helper(r+1, n, sCol, sD1, sD2)
			//  board[r][i]=false
			sCol[i] = false
			sD1[i+r] = false
			sD2[(r-i)+n] = false
		}
	}
	return res
}
