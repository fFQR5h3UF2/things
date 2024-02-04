// Submission for Intersection of Two Arrays II
// Submission url: https://leetcode.com/submissions/detail/692919579/

package submissions

func intersect(numbers_1 []int, numbers_2 []int) (result []int) {
	length_biggest := len(numbers_1)
	if len(numbers_2) > length_biggest {
		length_biggest = len(numbers_2)
	}
	count := make([]int, length_biggest)
	for _, number := range numbers_1 {
		count[number]++
	}
	for _, number := range numbers_2 {
		if count[number] <= 0 {
			continue
		}
		count[number]--
		result = append(result, number)
	}
	return
}
