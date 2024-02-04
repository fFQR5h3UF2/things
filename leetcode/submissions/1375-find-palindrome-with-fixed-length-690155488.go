// Submission for Find Palindrome With Fixed Length
// Submission url: https://leetcode.com/submissions/detail/690155488/

package submissions

import "fmt"
import "math"
func kthPalindrome(queries []int, intLength int) (answer []int64) {
	var highest int
	for _, query := range queries {
		if query > highest {
			highest = query
		}
	}
	palindromes := constructPalindromes(intLength, highest)
    fmt.Println(palindromes)
	for _, query := range queries {
		var palindrom int64
		if query > len(palindromes) {
			palindrom = -1
		} else {
			palindrom = fromList(palindromes[query-1])
		}
		answer = append(answer, palindrom)
	}
	return
}



func constructPalindromes(length int, highest int) [][]int {
	palindromes := [][]int{toList(int64(math.Pow10(length))/10 + 1)}
	middle, even := length/2, length%2 == 0
	for {
		index := middle
		if !even {
			index -= 1
			new := make([]int, length)
			copy(new, palindromes[len(palindromes)-1])
			if new[middle] < 9 {
				new[middle] += 1
				palindromes = append(palindromes, new)
				continue
			} else if palindromes[len(palindromes)-1][0] == 9 {
				return palindromes
			} else {
				new[middle] = 0
				new[0] += 1
				new[length-1] += 1
				palindromes = append(palindromes, new)
			}
		}
		for ; index > 0; index-- {
			for count := 0; count < 10; count++ {
				current_length := len(palindromes)
				new_loop := make([]int, length)
				copy(new_loop, palindromes[current_length-1])
				new_loop[index] += 1
				new_loop[length-index-1] += 1
				palindromes = append(palindromes, new_loop)
				if current_length >= highest {
					return palindromes
				}
			}
		}
	}
}



func toList(number int64) (result []int) {
	if number/10 == 0 {
		return []int{int(number)}
	}
	current := number
	for {
		if current == 0 {
			return
		}
		result = append(result, int(current%10))
		current /= 10
	}
}

func fromList(number []int) (result int64) {
	for index, digit := range number {
		result += int64(digit) * int64(math.Pow10(index))
	}
	return
}
