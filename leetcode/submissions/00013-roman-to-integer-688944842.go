// Submission title: for Roman to Integer
// Submission url  : https://leetcode.com/submissions/detail/688944842/
// Submission json : {"id": 688944842, "status_display": "Accepted", "lang": "golang", "question_id": 13, "title_slug": "roman-to-integer", "code": "\nfunc in(character rune, targets string) bool {\n\tfor _, target := range targets {\n\t\tif character == target {\n\t\t\treturn true\n\t\t}\n\t}\n\treturn false\n}\n\nfunc romanToInt(roman string) int {\n\ttype dict map[rune]int\n\tvar result int\n\tinput := []rune(roman)\n\ttypes := dict{\n\t\t'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,\n\t}\n\tvar previous rune\n\tfor _, character := range input {\n\t\tresult += types[character]\n\t\tswitch {\n\t\tcase previous == 'I' && in(character, \"VX\"):\n\t\t\tfallthrough\n\t\tcase previous == 'X' && in(character, \"LC\"):\n\t\t\tfallthrough\n\t\tcase previous == 'C' && in(character, \"DM\"):\n\t\t\tresult -= types[previous] * 2\n\t\t}\n\t\tprevious = character\n\t}\n\treturn result\n}\n", "title": "Roman to Integer", "url": "/submissions/detail/688944842/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651125574, "status": 10, "runtime": "31 ms", "is_pending": "Not Pending", "memory": "2.9 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func in(character rune, targets string) bool {
	for _, target := range targets {
		if character == target {
			return true
		}
	}
	return false
}

func romanToInt(roman string) int {
	type dict map[rune]int
	var result int
	input := []rune(roman)
	types := dict{
		'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
	}
	var previous rune
	for _, character := range input {
		result += types[character]
		switch {
		case previous == 'I' && in(character, "VX"):
			fallthrough
		case previous == 'X' && in(character, "LC"):
			fallthrough
		case previous == 'C' && in(character, "DM"):
			result -= types[previous] * 2
		}
		previous = character
	}
	return result
}