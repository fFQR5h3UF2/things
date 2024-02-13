// Submission title: Eliminate Maximum Number of Monsters
// Submission url  : https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/
// Submission url  : https://leetcode.com/submissions/detail/1093720985/
// Submission json : {"id":1093720985,"status_display":"Accepted","lang":"golang","question_id":2049,"title_slug":"eliminate-maximum-number-of-monsters","code":"func eliminateMaximum(dist []int, speed []int) int {\n    arrival := []float32{}\n    length := len(dist)\n    for i := 0; i < length; i++ {\n        arrival = append(arrival, float32(dist[i]) / float32(speed[i]))\n    }\n    slices.Sort(arrival)\n    ans := 0\n    for i := 0; i < length; i++ {\n        if arrival[i] <= float32(i) {\n            break\n        }\n        ans += 1\n    }\n    return ans\n}","title":"Eliminate Maximum Number of Monsters","url":"/submissions/detail/1093720985/","lang_name":"Go","time":"2 months, 4 weeks","timestamp":1699373268,"status":10,"runtime":"103 ms","is_pending":"Not Pending","memory":"8.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func eliminateMaximum(dist []int, speed []int) int {
	arrival := []float32{}
	length := len(dist)
	for i := 0; i < length; i++ {
		arrival = append(arrival, float32(dist[i])/float32(speed[i]))
	}
	slices.Sort(arrival)
	ans := 0
	for i := 0; i < length; i++ {
		if arrival[i] <= float32(i) {
			break
		}
		ans += 1
	}
	return ans
}
