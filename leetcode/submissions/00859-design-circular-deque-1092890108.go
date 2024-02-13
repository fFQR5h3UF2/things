// Submission title: Design Circular Deque
// Submission url  : https://leetcode.com/problems/design-circular-deque/description/
// Submission url  : https://leetcode.com/submissions/detail/1092890108/
// Submission json : {"id":1092890108,"status_display":"Accepted","lang":"golang","question_id":859,"title_slug":"design-circular-deque","code":"type MyCircularDeque struct {\n    list []int\n    size int\n}\n\n\nfunc Constructor(k int) MyCircularDeque {\n    return MyCircularDeque{[]int{}, k}\n}\n\n\nfunc (this *MyCircularDeque) InsertFront(value int) bool {\n    if this.IsFull() {\n        return false\n    }\n    this.list = append([]int{value}, this.list...)\n    return true\n}\n\n\nfunc (this *MyCircularDeque) InsertLast(value int) bool {\n    if this.IsFull() {\n        return false\n    }\n    this.list = append(this.list, value)\n    return true\n}\n\n\nfunc (this *MyCircularDeque) DeleteFront() bool {\n    if this.IsEmpty() {\n        return false\n    }\n    this.list = this.list[1:]\n    return true\n}\n\n\nfunc (this *MyCircularDeque) DeleteLast() bool {\n    if this.IsEmpty() {\n        return false\n    }\n    this.list = this.list[:len(this.list) - 1]\n    return true\n}\n\n\nfunc (this *MyCircularDeque) GetFront() int {\n    if this.IsEmpty() {\n        return -1\n    }\n    return this.list[0]   \n}\n\n\nfunc (this *MyCircularDeque) GetRear() int {\n    if this.IsEmpty() {\n        return -1\n    }\n    return this.list[len(this.list) - 1]\n}\n\n\nfunc (this *MyCircularDeque) IsEmpty() bool {\n    return len(this.list) == 0\n}\n\n\nfunc (this *MyCircularDeque) IsFull() bool {\n    return len(this.list) == this.size\n}\n\n\n/**\n * Your MyCircularDeque object will be instantiated and called as such:\n * obj := Constructor(k);\n * param_1 := obj.InsertFront(value);\n * param_2 := obj.InsertLast(value);\n * param_3 := obj.DeleteFront();\n * param_4 := obj.DeleteLast();\n * param_5 := obj.GetFront();\n * param_6 := obj.GetRear();\n * param_7 := obj.IsEmpty();\n * param_8 := obj.IsFull();\n */","title":"Design Circular Deque","url":"/submissions/detail/1092890108/","lang_name":"Go","time":"2 months, 4 weeks","timestamp":1699285294,"status":10,"runtime":"8 ms","is_pending":"Not Pending","memory":"7.1 MB","compare_result":"111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}
package submissions

type MyCircularDeque struct {
	list []int
	size int
}

func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{[]int{}, k}
}

func (this *MyCircularDeque) InsertFront(value int) bool {
	if this.IsFull() {
		return false
	}
	this.list = append([]int{value}, this.list...)
	return true
}

func (this *MyCircularDeque) InsertLast(value int) bool {
	if this.IsFull() {
		return false
	}
	this.list = append(this.list, value)
	return true
}

func (this *MyCircularDeque) DeleteFront() bool {
	if this.IsEmpty() {
		return false
	}
	this.list = this.list[1:]
	return true
}

func (this *MyCircularDeque) DeleteLast() bool {
	if this.IsEmpty() {
		return false
	}
	this.list = this.list[:len(this.list)-1]
	return true
}

func (this *MyCircularDeque) GetFront() int {
	if this.IsEmpty() {
		return -1
	}
	return this.list[0]
}

func (this *MyCircularDeque) GetRear() int {
	if this.IsEmpty() {
		return -1
	}
	return this.list[len(this.list)-1]
}

func (this *MyCircularDeque) IsEmpty() bool {
	return len(this.list) == 0
}

func (this *MyCircularDeque) IsFull() bool {
	return len(this.list) == this.size
}

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * obj := Constructor(k);
 * param_1 := obj.InsertFront(value);
 * param_2 := obj.InsertLast(value);
 * param_3 := obj.DeleteFront();
 * param_4 := obj.DeleteLast();
 * param_5 := obj.GetFront();
 * param_6 := obj.GetRear();
 * param_7 := obj.IsEmpty();
 * param_8 := obj.IsFull();
 */
