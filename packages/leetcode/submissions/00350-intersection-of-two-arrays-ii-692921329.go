// Submission title: for Intersection of Two Arrays II
// Submission url  : https://leetcode.com/submissions/detail/692921329/
// Submission json : {"id": 692921329, "status_display": "Accepted", "lang": "golang", "question_id": 350, "title_slug": "intersection-of-two-arrays-ii", "code": "\nfunc intersect(numbers_1 []int, numbers_2 []int) (result []int) {\n\t// 0 <= nums1[i], nums2[i] <= 1000\n\tcount := make([]int, 1001)\n\t// counting how many times a number occured in the first array\n\tfor _, number := range numbers_1 {\n\t\tcount[number]++\n\t}\n\tfor _, number := range numbers_2 {\n\t\t// the number did not occur in the first array\n\t\t// -> ignoring it\n\t\tif count[number] <= 0 {\n\t\t\tcontinue\n\t\t}\n\t\tcount[number]--\n\t\tresult = append(result, number)\n\t}\n\treturn\n}", "title": "Intersection of Two Arrays II", "url": "/submissions/detail/692921329/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651658051, "status": 10, "runtime": "5 ms", "is_pending": "Not Pending", "memory": "2.8 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

func intersect(numbers_1 []int, numbers_2 []int) (result []int) {
	// 0 <= nums1[i], nums2[i] <= 1000
	count := make([]int, 1001)
	// counting how many times a number occured in the first array
	for _, number := range numbers_1 {
		count[number]++
	}
	for _, number := range numbers_2 {
		// the number did not occur in the first array
		// -> ignoring it
		if count[number] <= 0 {
			continue
		}
		count[number]--
		result = append(result, number)
	}
	return
}
