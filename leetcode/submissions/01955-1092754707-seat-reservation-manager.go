// Submission title: Seat Reservation Manager
// Submission url  : https://leetcode.com/problems/seat-reservation-manager/description/
// Submission url  : https://leetcode.com/submissions/detail/1092754707/"
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
