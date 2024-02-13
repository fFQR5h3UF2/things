// Submission title: Move Zeroes
// Submission url  : https://leetcode.com/problems/move-zeroes/description/
// Submission url  : https://leetcode.com/submissions/detail/693605143/
// Submission json : {"id":693605143,"status_display":"Accepted","lang":"golang","question_id":283,"title_slug":"move-zeroes","code":"func moveZeroes(nums []int)  {\n    count:=0\n    for i:=0; i<len(nums);i++{\n        if nums[i] == 0{\n            count++\n        }else{\n            nums[i-count]=nums[i]\n        }\n    }\n    for count>0{\n        nums[len(nums)-count] = 0\n        count--\n    }\n    \n    \n}","title":"Move Zeroes","url":"/submissions/detail/693605143/","lang_name":"Go","time":"1 year, 9 months","timestamp":1651747146,"status":10,"runtime":"32 ms","is_pending":"Not Pending","memory":"6.9 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

func moveZeroes(nums []int) {
	count := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			count++
		} else {
			nums[i-count] = nums[i]
		}
	}
	for count > 0 {
		nums[len(nums)-count] = 0
		count--
	}

}
