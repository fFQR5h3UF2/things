// Submission title: Seat Reservation Manager
// Submission url  : https://leetcode.com/problems/seat-reservation-manager/description/
// Submission url  : https://leetcode.com/submissions/detail/1092750852/
// Submission json : {"id":1092750852,"status_display":"Accepted","lang":"golang","question_id":1955,"title_slug":"seat-reservation-manager","code":"type SeatManager struct {\n    seats []bool\n}\n\n\nfunc Constructor(n int) SeatManager {\n    return SeatManager{make([]bool, n)}\n}\n\n\nfunc (this *SeatManager) Reserve() int {\n    for i, num := range this.seats {\n        if !num {\n            this.seats[i] = true\n            return i + 1\n        }\n    }\n    return -1\n}\n\n\nfunc (this *SeatManager) Unreserve(seatNumber int)  {\n    this.seats[seatNumber-1] = false\n}\n\n\n/**\n * Your SeatManager object will be instantiated and called as such:\n * obj := Constructor(n);\n * param_1 := obj.Reserve();\n * obj.Unreserve(seatNumber);\n */","title":"Seat Reservation Manager","url":"/submissions/detail/1092750852/","lang_name":"Go","time":"3 months","timestamp":1699271367,"status":10,"runtime":"2383 ms","is_pending":"Not Pending","memory":"29 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}
package submissions

type SeatManager struct {
	seats []bool
}

func Constructor(n int) SeatManager {
	return SeatManager{make([]bool, n)}
}

func (this *SeatManager) Reserve() int {
	for i, num := range this.seats {
		if !num {
			this.seats[i] = true
			return i + 1
		}
	}
	return -1
}

func (this *SeatManager) Unreserve(seatNumber int) {
	this.seats[seatNumber-1] = false
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
