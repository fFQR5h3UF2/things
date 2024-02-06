// Submission title: for Merge Sorted Array
// Submission url  : https://leetcode.com/submissions/detail/692799831/
// Submission json : {"id": 692799831, "status_display": "Accepted", "lang": "golang", "question_id": 88, "title_slug": "merge-sorted-array", "code": "\nfunc merge(array1 []int, length1 int, array2 []int, length2 int) {\n\tif length2 == 0 {\n\t\treturn\n\t}\n\tif length1 == 0 {\n\t\tfor index, number := range array2 {\n\t\t\tarray1[index] = number\n\t\t}\n\t\treturn\n\t}\n\tindex1, index2, array1Copy := 0, 0, make([]int, length1)\n\tcopy(array1Copy, array1)\n\tfor index := 0; index < length1+length2; index++ {\n\t\tfmt.Println(index, index1, index2, array1, array2)\n\t\tfor index2 < length2 && (index1 >= length1 || array2[index2] <= array1Copy[index1]) {\n\t\t\tarray1[index] = array2[index2]\n\t\t\tindex2++\n\t\t\tindex++\n\t\t}\n\t\tif index1 >= length1 {\n\t\t\tcontinue\n\t\t}\n\t\tarray1[index] = array1Copy[index1]\n\t\tindex1++\n\t}\n}\n", "title": "Merge Sorted Array", "url": "/submissions/detail/692799831/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651642416, "status": 10, "runtime": "27 ms", "is_pending": "Not Pending", "memory": "4.9 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func merge(array1 []int, length1 int, array2 []int, length2 int) {
	if length2 == 0 {
		return
	}
	if length1 == 0 {
		for index, number := range array2 {
			array1[index] = number
		}
		return
	}
	index1, index2, array1Copy := 0, 0, make([]int, length1)
	copy(array1Copy, array1)
	for index := 0; index < length1+length2; index++ {
		fmt.Println(index, index1, index2, array1, array2)
		for index2 < length2 && (index1 >= length1 || array2[index2] <= array1Copy[index1]) {
			array1[index] = array2[index2]
			index2++
			index++
		}
		if index1 >= length1 {
			continue
		}
		array1[index] = array1Copy[index1]
		index1++
	}
}
