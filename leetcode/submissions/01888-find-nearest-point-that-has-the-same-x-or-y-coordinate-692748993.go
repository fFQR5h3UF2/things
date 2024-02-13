// Submission title: Find Nearest Point That Has the Same X or Y Coordinate
// Submission url  : https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/
// Submission url  : https://leetcode.com/submissions/detail/692748993/
// Submission json : {"id":692748993,"status_display":"Accepted","lang":"golang","question_id":1888,"title_slug":"find-nearest-point-that-has-the-same-x-or-y-coordinate","code":"func nearestValidPoint(x int, y int, points [][]int) int {\n\tpoint_target, smallest_distance, smallest_index := []int{x, y}, math.MaxInt, -1\n\tfor index, point := range points {\n\t\t// ignore the point if it is not valid\n\t\tif !valid(point_target, point) {\n\t\t\tcontinue\n\t\t}\n\t\tdistance := distance(point_target, point)\n\t\t// ignore the point if its Manhattan distance is bigger\n\t\tif distance >= smallest_distance {\n\t\t\tcontinue\n\t\t}\n\t\t// the distance is smaller, update the index and the distance\n\t\tsmallest_index, smallest_distance = index, distance\n\t}\n\t// there are no valid points\n\tif smallest_index == -1 {\n\t\treturn -1\n\t}\n\treturn smallest_index\n}\n\nfunc valid(point_target []int, point []int) bool {\n\tswitch {\n\tcase point_target[0] == point[0]:\n\t\tfallthrough\n\tcase point_target[1] == point[1]:\n\t\treturn true\n\tdefault:\n\t\treturn false\n\t}\n}\n\nfunc distance(point_target []int, point []int) int {\n\treturn abs(point_target[0]-point[0]) + abs(point_target[1]-point[1])\n}\n\nfunc abs(number int) int {\n\tif number < 0 {\n\t\treturn number * -1\n\t}\n\treturn number\n}\n","title":"Find Nearest Point That Has the Same X or Y Coordinate","url":"/submissions/detail/692748993/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651637011,"status":10,"runtime":"301 ms","is_pending":"Not Pending","memory":"7.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func nearestValidPoint(x int, y int, points [][]int) int {
	point_target, smallest_distance, smallest_index := []int{x, y}, math.MaxInt, -1
	for index, point := range points {
		// ignore the point if it is not valid
		if !valid(point_target, point) {
			continue
		}
		distance := distance(point_target, point)
		// ignore the point if its Manhattan distance is bigger
		if distance >= smallest_distance {
			continue
		}
		// the distance is smaller, update the index and the distance
		smallest_index, smallest_distance = index, distance
	}
	// there are no valid points
	if smallest_index == -1 {
		return -1
	}
	return smallest_index
}

func valid(point_target []int, point []int) bool {
	switch {
	case point_target[0] == point[0]:
		fallthrough
	case point_target[1] == point[1]:
		return true
	default:
		return false
	}
}

func distance(point_target []int, point []int) int {
	return abs(point_target[0]-point[0]) + abs(point_target[1]-point[1])
}

func abs(number int) int {
	if number < 0 {
		return number * -1
	}
	return number
}
