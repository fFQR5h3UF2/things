// Submission title: Move Zeroes
// Submission url  : https://leetcode.com/problems/move-zeroes/description/
// Submission url  : https://leetcode.com/submissions/detail/693604925/
// Submission json : {"id":693604925,"status_display":"Accepted","lang":"golang","question_id":283,"title_slug":"move-zeroes","code":"func moveZeroes(nums []int)  {\n    \tif len(nums) < 2 {\n\t\treturn\n\t}\n\n\tfor z, p := 0, 1; p < len(nums) && z < len(nums); {\n\t\tif nums[z] == 0 && nums[p] != 0 {\n\t\t\tif p > z {\n\t\t\t\tnums[z], nums[p] = nums[p], nums[z]\n\t\t\t\tz++\n\t\t\t}\n\t\t\tp = z+1\n\t\t} else {\n\t\t\tif nums[z] != 0 {\n\t\t\t\tz++\n\t\t\t}\n\t\t\tif nums[p] == 0 {\n\t\t\t\tp++\n\t\t\t}\n\t\t}\n\t}\n\n}","title":"Move Zeroes","url":"/submissions/detail/693604925/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651747104,"status":10,"runtime":"137 ms","is_pending":"Not Pending","memory":"7.4 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func moveZeroes(nums []int) {
	if len(nums) < 2 {
		return
	}

	for z, p := 0, 1; p < len(nums) && z < len(nums); {
		if nums[z] == 0 && nums[p] != 0 {
			if p > z {
				nums[z], nums[p] = nums[p], nums[z]
				z++
			}
			p = z + 1
		} else {
			if nums[z] != 0 {
				z++
			}
			if nums[p] == 0 {
				p++
			}
		}
	}

}
