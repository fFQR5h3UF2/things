// Submission title: Basic Calculator
// Submission url  : https://leetcode.com/problems/basic-calculator/description/
// Submission url  : https://leetcode.com/submissions/detail/1091198199/
// Submission json : {"id":1091198199,"status_display":"Accepted","lang":"golang","question_id":224,"title_slug":"basic-calculator","code":"func calculate(s string) int {\n\tresult, _ := calculateFrom(s, 0)\n\treturn result\n}\n\nfunc calculateFrom(s string, idFrom int) (result, idEnd int) {\n\tresult, currNum, sign := 0, 0, 1\n\n\tfor idEnd = idFrom; idEnd < len(s) && s[idEnd] != ')'; idEnd++ {\n\t\tswitch {\n\t\tcase s[idEnd] >= '0':\n\t\t\tcurrNum = currNum*10 + int(s[idEnd]-'0')\n\t\tcase s[idEnd] == '(':\n\t\t\tcurrNum, idEnd = calculateFrom(s, idEnd+1)\n\t\tcase s[idEnd] == '-' || s[idEnd] == '+':\n\t\t\tresult, currNum = result+currNum*sign, 0\n\t\t\tsign = 44 - int(s[idEnd]) // '-'=45; '+'=43\n\t\t}\n\t}\n\n\treturn result + currNum*sign, idEnd\n}","title":"Basic Calculator","url":"/submissions/detail/1091198199/","lang_name":"Go","time":"3 months","timestamp":1699093360,"status":10,"runtime":"3 ms","is_pending":"Not Pending","memory":"2.9 MB","compare_result":"111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func calculate(s string) int {
	result, _ := calculateFrom(s, 0)
	return result
}

func calculateFrom(s string, idFrom int) (result, idEnd int) {
	result, currNum, sign := 0, 0, 1

	for idEnd = idFrom; idEnd < len(s) && s[idEnd] != ')'; idEnd++ {
		switch {
		case s[idEnd] >= '0':
			currNum = currNum*10 + int(s[idEnd]-'0')
		case s[idEnd] == '(':
			currNum, idEnd = calculateFrom(s, idEnd+1)
		case s[idEnd] == '-' || s[idEnd] == '+':
			result, currNum = result+currNum*sign, 0
			sign = 44 - int(s[idEnd]) // '-'=45; '+'=43
		}
	}

	return result + currNum*sign, idEnd
}
