// Submission for Find Palindrome With Fixed Length
// Submission url: https://leetcode.com/submissions/detail/690293060/

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
	fmt.Println(*count, palendrom)
	if _, exists := queries[*count]; !exists {
		return
	}
	delete(queries, *count)
	new_palendrom := make([]int, length)
	copy(new_palendrom, palendrom)
	palendromes[*count] = fromList(new_palendrom)

}

func constructPalindromes(length int, queries map[int]bool) map[int]int64 {
	palindromes := make(map[int]int64, len(queries))
	if length == 0 {
		return palindromes
	} else if length == 1 {
		for index := 0; index < 10; index++ {
			palindromes[index] = int64(index)
		}
		return palindromes
	}
	root := math.Pow10(length) / 10
	if root != 1 {
		root += 1
	}
	count_max := int(math.Pow10(1 + length/2))
	middle, is_uneven := length/2, length%2 != 0
	last, count := toList(int(root)), new(int)
	updateQueries(count, length, last, queries, palindromes)
	for {
		switch {
		case last[middle] == 9 && last[0] == 9:
			fallthrough
		case len(queries) == 0 || *count > count_max:
			return palindromes
		case is_uneven && last[middle] < 9:
			last[middle] += 1
			updateQueries(count, length, last, queries, palindromes)
			continue
		case is_uneven && last[middle] == 9:
			last[middle] = 0
		}
		for index := middle - 1; index >= 0; index-- {
		//	fmt.Println("index", index)
			if last[index] == 9 {
				last[index] = 0
				last[length-index-1] = 0
				continue
			}
			if last[index] < 9 {
				last[index]++
				last[length-index-1]++
				updateQueries(count, length, last, queries, palindromes)
				if len(queries) == 0 || *count > count_max {
					return palindromes
				}
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
