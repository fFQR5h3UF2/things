// Submission title: Find The Original Array of Prefix Xor
// Submission url  : https://leetcode.com/problems/find-the-original-array-of-prefix-xor/description/
// Submission url  : https://leetcode.com/submissions/detail/1088205030/
// Submission json : {"id":1088205030,"status_display":"Accepted","lang":"golang","question_id":2519,"title_slug":"find-the-original-array-of-prefix-xor","code":"func findArray(pref []int) []int {\n    prev := pref[0]\n    for i := 1; i < len(pref); i++ {\n        prev, pref[i] = pref[i], prev ^ pref[i] \n    }\n    return pref\n}","title":"Find The Original Array of Prefix Xor","url":"/submissions/detail/1088205030/","lang_name":"Go","time":"3 months","timestamp":1698741160,"status":10,"runtime":"104 ms","is_pending":"Not Pending","memory":"8.6 MB","compare_result":"1111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func findArray(pref []int) []int {
	prev := pref[0]
	for i := 1; i < len(pref); i++ {
		prev, pref[i] = pref[i], prev^pref[i]
	}
	return pref
}
