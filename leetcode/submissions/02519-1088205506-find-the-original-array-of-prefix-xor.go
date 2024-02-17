// Submission title: Find The Original Array of Prefix Xor
// Submission url  : https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/"
// Submission url  : https://leetcode.com/submissions/detail/1088205506/"
package submissions

func findArray(pref []int) []int {
	prev := pref[0]
	for i := 1; i < len(pref); i++ {
		cur := pref[i]
		prev, pref[i] = cur, prev^cur
	}
	return pref
}
