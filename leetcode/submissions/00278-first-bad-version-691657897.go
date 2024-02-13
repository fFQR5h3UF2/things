// Submission title: First Bad Version
// Submission url  : https://leetcode.com/problems/first-bad-version/description/
// Submission url  : https://leetcode.com/submissions/detail/691657897/
// Submission json : {"id":691657897,"status_display":"Accepted","lang":"golang","question_id":278,"title_slug":"first-bad-version","code":"\nfunc firstBadVersion(n int) int {\n\t// checking edge cases\n\tif isBadVersion(1) {\n\t\treturn 1\n\t}\n\tleft, right, bad_version := 1, n, math.MaxInt\n\tfor right >= left {\n\t\t// overflow protection\n\t\tversion := left + (right-left)/2\n\t\tswitch isBadVersion(version) {\n\t\tcase false:\n\t\t\t// it is good -> versions to the left are good -> discard left\n\t\t\tleft = version + 1\n\t\tcase true:\n\t\t\t// it is bad -> the first bad version is either this one or to the left\n\t\t\t// discard right\n\t\t\tbad_version = version\n\t\t\tright = version - 1\n\t\t}\n\t}\n\t// the search space is empty\n\treturn bad_version\n}\n","title":"First Bad Version","url":"/submissions/detail/691657897/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651503755,"status":10,"runtime":"0 ms","is_pending":"Not Pending","memory":"1.9 MB","compare_result":"1111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func firstBadVersion(n int) int {
	// checking edge cases
	if isBadVersion(1) {
		return 1
	}
	left, right, bad_version := 1, n, math.MaxInt
	for right >= left {
		// overflow protection
		version := left + (right-left)/2
		switch isBadVersion(version) {
		case false:
			// it is good -> versions to the left are good -> discard left
			left = version + 1
		case true:
			// it is bad -> the first bad version is either this one or to the left
			// discard right
			bad_version = version
			right = version - 1
		}
	}
	// the search space is empty
	return bad_version
}
