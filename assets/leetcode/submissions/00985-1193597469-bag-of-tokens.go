// Submission title: Bag of Tokens
// Submission url  : https://leetcode.com/problems/bag-of-tokens/description/
// Submission url  : https://leetcode.com/submissions/detail/1193597469/"
package submissions

func bagOfTokensScore(tokens []int, power int) int {
	n := len(tokens)
	sort.Ints(tokens)
	res := 0

	l := 0
	r := n - 1

	for l <= r {
		for l <= r && power >= tokens[l] {
			power -= tokens[l]
			l++
			res++
		}

		if res == 0 {
			break
		}

		if r-l+1 <= 2 {
			break
		}

		power += tokens[r]
		r--
		res--
	}

	return res
}
