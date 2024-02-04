// Submission for Find Palindrome With Fixed Length
// Submission url: https://leetcode.com/submissions/detail/690222741/

package submissions

//import "fmt"
import "math"


func kthPalindrome(queries []int, intLength int) (answer []int64) {
	queries_map := make(map[int]bool, len(queries))
	for _, query := range queries {
		queries_map[query] = true
	}
	palindromes := constructPalindromes(intLength, queries_map)
	for _, query := range queries {
		palindrom, exists := palindromes[query]
		if !exists {
			palindrom = -1
		}
		answer = append(answer, palindrom)
	}
	return
}

func updateQueries(count *int, length int, palendrom []int, queries map[int]bool, palendromes map[int]int64) {
	*count++
	//fmt.Println(*count, palendrom)
	if _, exists := queries[*count]; !exists {
		return
	}
	delete(queries, *count)
	new_palendrom := make([]int, length)
	copy(new_palendrom, palendrom)
	palendromes[*count] = fromList(new_palendrom)

}

func constructPalindromes(length int, queries map[int]bool) map[int]int64 {
	root := math.Pow10(length) / 10
	if root != 1 {
		root += 1
	}
	palindromes := make(map[int]int64, len(queries))
	middle, is_uneven := length/2, length%2 != 0
	last, count := toList(int(root)), new(int)
	updateQueries(count, length, last, queries, palindromes)
	for {
		middle_corrected := middle
		switch {
		case len(queries) == 0 || last[0] == 9:
			return palindromes
		case is_uneven && last[middle] < 9:
			last[middle] += 1
			updateQueries(count, length, last, queries, palindromes)
			continue
		case is_uneven && last[middle] == 9:
			middle_corrected -= 1
			last[middle] = 0
		}
		for index := middle_corrected; index < length; index++ {
			if last[index] < 9 {
				last[index]++
				last[length-index-1]++
				updateQueries(count, length, last, queries, palindromes)
				if len(queries) == 0 {
					return palindromes
				}
			}
			is_9 := last[index] == 9
			if is_9 && index == length-1 {
				return palindromes
			} else if is_9 && !is_uneven {
				last[index] = 0
				last[length-index-1] = 0
				continue
			}
			break
		}
	}
}

func toList(number int) (result []int) {
	if number/10 == 0 {
		return []int{number}
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
