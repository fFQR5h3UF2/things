// Submission title: Merge Sorted Array
// Submission url  : https://leetcode.com/problems/merge-sorted-array/description/
// Submission url  : https://leetcode.com/submissions/detail/690860583/
// Submission json : {"id":690860583,"status_display":"Accepted","lang":"golang","question_id":88,"title_slug":"merge-sorted-array","code":"\nfunc merge(array1 []int, length1 int, array2 []int, length2 int) {\n\tindex1, index2, array1Copy := 0, 0, make([]int, length1)\n\tcopy(array1Copy, array1)\n\tfor index := 0; index < length1+length2; index++ {\n\t\tfmt.Println(index, index1, index2, array1, array2)\n\t\tif index2 < length2 && (index1 >= length1 || array2[index2] <= array1Copy[index1]) {\n\t\t\tarray1[index] = array2[index2]\n\t\t\tindex2++\n\t\t\tcontinue\n\t\t}\n\t\tarray1[index] = array1Copy[index1]\n\t\tindex1++\n\n\t}\n}","title":"Merge Sorted Array","url":"/submissions/detail/690860583/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651399964,"status":10,"runtime":"97 ms","is_pending":"Not Pending","memory":"6.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func merge(array1 []int, length1 int, array2 []int, length2 int) {
	index1, index2, array1Copy := 0, 0, make([]int, length1)
	copy(array1Copy, array1)
	for index := 0; index < length1+length2; index++ {
		fmt.Println(index, index1, index2, array1, array2)
		if index2 < length2 && (index1 >= length1 || array2[index2] <= array1Copy[index1]) {
			array1[index] = array2[index2]
			index2++
			continue
		}
		array1[index] = array1Copy[index1]
		index1++

	}
}
