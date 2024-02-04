# Submission for 'Merge Sorted Array'
# Submission url: https://leetcode.com/submissions/detail/690860583/


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
