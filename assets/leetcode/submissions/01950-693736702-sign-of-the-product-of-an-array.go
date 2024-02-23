// Submission title: Sign of the Product of an Array
// Submission url  : https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
// Submission url  : https://leetcode.com/submissions/detail/693736702/"
package submissions

func arraySign(numbers []int) int {
	negative_count := 0
	for _, number := range numbers {
		switch {
		// the number is 0 -> product of all numbers is definitely zero
		case number == 0:
			return 0
			// the number is negative -> add to count
		case number < 0:
			negative_count++
		}
	}
	// even amount of negative numbers -> result is positive
	if negative_count&1 == 0 {
		return 1
	}
	// uneven amount of negative numbers -> result is negative
	return -1
}
