// Submission for Intersection of Two Arrays II
// Submission url: https://leetcode.com/submissions/detail/692919844/

package submissions


func intersect(numbers_1 []int, numbers_2 []int) (result []int) {
	count := make([]int, len(numbers_1)+len(numbers_2))
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
