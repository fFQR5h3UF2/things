// Submission for Find The Original Array of Prefix Xor
// Submission url: https://leetcode.com/submissions/detail/1088205030/

package submissions

func findArray(pref []int) []int {
	prev := pref[0]
	for i := 1; i < len(pref); i++ {
		prev, pref[i] = pref[i], prev^pref[i]
	}
	return pref
}
