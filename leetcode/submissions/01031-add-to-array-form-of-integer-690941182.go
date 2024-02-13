// Submission title: Add to Array-Form of Integer
// Submission url  : https://leetcode.com/problems/add-to-array-form-of-integer/description/
// Submission url  : https://leetcode.com/submissions/detail/690941182/
// Submission json : {"id":690941182,"status_display":"Accepted","lang":"golang","question_id":1031,"title_slug":"add-to-array-form-of-integer","code":"func addToArrayForm(number1 []int, add int) []int {\n\tif add == 0 {\n\t\treturn number1\n\t}\n\tif len(number1) == 0 {\n\t\treturn convert(add)\n\t}\n\tnumber2 := convert(add)\n\tlength1, length2, carry := len(number1), len(number2), 0\n\thightest := length1\n\tif length2 > length1 {\n\t\thightest = length2\n\t}\n\tresult := make([]int, hightest)\n\tindex1, index2, indexResult := length1-1, 0, hightest-1\n\tfor {\n\t\tindex1Valid, index2Valid := index1 >= 0, index2 < length2\n\t\tif !index1Valid && !index2Valid && carry==0 {\n\t\t\tbreak\n\t\t}\n\t\tdigit1, digit2 := 0, 0\n\t\tif index1Valid {\n\t\t\tdigit1 = number1[index1]\n\t\t\tindex1--\n\t\t}\n\t\tif index2Valid {\n\t\t\tdigit2 = number2[index2]\n\t\t\tindex2++\n\t\t}\n\t\tdigitResult := digit1 + digit2 + carry\n\t\tif digitResult > 9 {\n\t\t\tcarry = 1\n\t\t\tdigitResult -= 10\n\t\t} else {\n\t\t\tcarry = 0\n\t\t}\n\t\tif indexResult == -1 {\n\t\t\tresult = append(result, 0)\n\t\t\tcopy(result[1:], result[0:hightest])\n            indexResult=0\n\t\t}\n\t\tresult[indexResult] = digitResult\n\t\tindexResult--\n\t}\n\treturn result\n}\n\nfunc convert(number int) (result []int) {\n\tfor {\n\t\tif number == 0 {\n\t\t\treturn\n\t\t}\n\t\tresult = append(result, number%10)\n\t\tnumber /= 10\n\t}\n}\n","title":"Add to Array-Form of Integer","url":"/submissions/detail/690941182/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651411437,"status":10,"runtime":"64 ms","is_pending":"Not Pending","memory":"7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func addToArrayForm(number1 []int, add int) []int {
	if add == 0 {
		return number1
	}
	if len(number1) == 0 {
		return convert(add)
	}
	number2 := convert(add)
	length1, length2, carry := len(number1), len(number2), 0
	hightest := length1
	if length2 > length1 {
		hightest = length2
	}
	result := make([]int, hightest)
	index1, index2, indexResult := length1-1, 0, hightest-1
	for {
		index1Valid, index2Valid := index1 >= 0, index2 < length2
		if !index1Valid && !index2Valid && carry == 0 {
			break
		}
		digit1, digit2 := 0, 0
		if index1Valid {
			digit1 = number1[index1]
			index1--
		}
		if index2Valid {
			digit2 = number2[index2]
			index2++
		}
		digitResult := digit1 + digit2 + carry
		if digitResult > 9 {
			carry = 1
			digitResult -= 10
		} else {
			carry = 0
		}
		if indexResult == -1 {
			result = append(result, 0)
			copy(result[1:], result[0:hightest])
			indexResult = 0
		}
		result[indexResult] = digitResult
		indexResult--
	}
	return result
}

func convert(number int) (result []int) {
	for {
		if number == 0 {
			return
		}
		result = append(result, number%10)
		number /= 10
	}
}
