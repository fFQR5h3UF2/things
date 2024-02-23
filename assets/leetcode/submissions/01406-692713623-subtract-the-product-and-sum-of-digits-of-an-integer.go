// Submission title: Subtract the Product and Sum of Digits of an Integer
// Submission url  : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
// Submission url  : https://leetcode.com/submissions/detail/692713623/"
package submissions

func subtractProductAndSum(number int) int {
	fist_digit := number % 10
	factorial, sum := fist_digit, fist_digit
	number /= 10
	for number > 0 {
		digit := number % 10
		factorial *= digit
		sum += digit
		number /= 10
	}
	return factorial - sum
}
