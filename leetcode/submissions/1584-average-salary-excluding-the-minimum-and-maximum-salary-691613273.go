# Submission for 'Average Salary Excluding the Minimum and Maximum Salary'
# Submission url: https://leetcode.com/submissions/detail/691613273/


func average(salary []int) float64 {
	length := len(salary)
	highest, lowest := math.MinInt, math.MaxInt
	result := 0
	for _, number := range salary {
		result += number
		if number > highest {
			highest = number
		}
		if number < lowest {
			lowest = number
		}
	}
	return float64(result-highest-lowest) / float64(length-2)
}
