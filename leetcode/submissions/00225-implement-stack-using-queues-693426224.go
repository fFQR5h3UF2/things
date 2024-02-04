// Submission title: for Implement Stack using Queues
// Submission url  : https://leetcode.com/submissions/detail/693426224/
// Submission json : {"id": 693426224, "status_display": "Accepted", "lang": "golang", "question_id": 225, "title_slug": "implement-stack-using-queues", "code": "\ntype MyStack struct{ queue *list.List }\n\nfunc Constructor() MyStack           { return MyStack{&list.List{}} }\nfunc (this *MyStack) Push(value int) { this.queue.PushFront(value) }\nfunc (this *MyStack) Top() int       { return this.queue.Front().Value.(int) }\nfunc (this *MyStack) Empty() bool    { return this.queue.Len() == 0 }\nfunc (this *MyStack) Pop() int {\n\treturn this.queue.Remove(this.queue.Front()).(int)\n}", "title": "Implement Stack using Queues", "url": "/submissions/detail/693426224/", "lang_name": "Go", "time": "1\u00a0year, 9\u00a0months", "timestamp": 1651723293, "status": 10, "runtime": "2 ms", "is_pending": "Not Pending", "memory": "2 MB", "compare_result": "1111111111111111", "has_notes": false, "flag_type": 1}

package submissions

type MyStack struct{ queue *list.List }

func Constructor() MyStack           { return MyStack{&list.List{}} }
func (this *MyStack) Push(value int) { this.queue.PushFront(value) }
func (this *MyStack) Top() int       { return this.queue.Front().Value.(int) }
func (this *MyStack) Empty() bool    { return this.queue.Len() == 0 }
func (this *MyStack) Pop() int {
	return this.queue.Remove(this.queue.Front()).(int)
}
