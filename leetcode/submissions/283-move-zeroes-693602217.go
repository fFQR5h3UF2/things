// Submission for Move Zeroes
// Submission url: https://leetcode.com/submissions/detail/693602217/

package submissions



func moveZeroes(numbers []int) {
	index_zero := -1
	// sliding window algorithm
	for index, number := range numbers {
		// if index_zero is not set, then the first zero is index_zero
		if index_zero == -1 && number == 0 {
			index_zero = index
		}
		// ignore zeros
		if number == 0 {
			continue
		}
		// after some zeros we encounter a non-zero number
		// moving that number to the beginning of zeros
		numbers[index_zero] = number
		// current number becomes zero
		numbers[index] = 0
		// moving the index
		index_zero++
	}
}
