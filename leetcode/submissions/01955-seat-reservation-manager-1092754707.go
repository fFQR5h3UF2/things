// Submission title: Seat Reservation Manager
// Submission url  : https://leetcode.com/problems/seat-reservation-manager/description/
// Submission url  : https://leetcode.com/submissions/detail/1092754707/
// Submission json : {"id":1092754707,"status_display":"Accepted","lang":"golang","question_id":1955,"title_slug":"seat-reservation-manager","code":"type SeatManager struct {\n    heap *binaryheap.Heap\n}\n\n\nfunc Constructor(n int) SeatManager {\n    heap := binaryheap.NewWithIntComparator()\n    for i := 1; i <= n; i++ {\n        heap.Push(i)\n    }\n    return SeatManager{heap}\n}\n\n\nfunc (this *SeatManager) Reserve() int {\n    val, _ := this.heap.Pop()\n    return val.(int)\n}\n\n\nfunc (this *SeatManager) Unreserve(seatNumber int)  {\n    this.heap.Push(seatNumber)\n}\n\n\n/**\n * Your SeatManager object will be instantiated and called as such:\n * obj := Constructor(n);\n * param_1 := obj.Reserve();\n * obj.Unreserve(seatNumber);\n */","title":"Seat Reservation Manager","url":"/submissions/detail/1092754707/","lang_name":"Go","time":"3 months","timestamp":1699271853,"status":10,"runtime":"379 ms","is_pending":"Not Pending","memory":"29.4 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}
package submissions

type SeatManager struct {
	heap *binaryheap.Heap
}

func Constructor(n int) SeatManager {
	heap := binaryheap.NewWithIntComparator()
	for i := 1; i <= n; i++ {
		heap.Push(i)
	}
	return SeatManager{heap}
}

func (this *SeatManager) Reserve() int {
	val, _ := this.heap.Pop()
	return val.(int)
}

func (this *SeatManager) Unreserve(seatNumber int) {
	this.heap.Push(seatNumber)
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Reserve();
 * obj.Unreserve(seatNumber);
 */
