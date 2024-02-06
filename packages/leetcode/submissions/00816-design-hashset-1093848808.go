// Submission title: for Design HashSet
// Submission url  : https://leetcode.com/submissions/detail/1093848808/
// Submission json : {"id": 1093848808, "status_display": "Accepted", "lang": "golang", "question_id": 816, "title_slug": "design-hashset", "code": "type MyHashSet struct {\n    m map[int]struct{}\n}\n\n\nfunc Constructor() MyHashSet {\n    return MyHashSet{map[int]struct{}{}}\n}\n\n\nfunc (this *MyHashSet) Add(key int)  {\n    this.m[key] = struct{}{}\n}\n\n\nfunc (this *MyHashSet) Remove(key int)  {\n    delete(this.m, key)\n}\n\n\nfunc (this *MyHashSet) Contains(key int) bool {\n    _, ok := this.m[key]\n    return ok\n}\n\n\n/**\n * Your MyHashSet object will be instantiated and called as such:\n * obj := Constructor();\n * obj.Add(key);\n * obj.Remove(key);\n * param_3 := obj.Contains(key);\n */", "title": "Design HashSet", "url": "/submissions/detail/1093848808/", "lang_name": "Go", "time": "2\u00a0months, 4\u00a0weeks", "timestamp": 1699383404, "status": 10, "runtime": "68 ms", "is_pending": "Not Pending", "memory": "8.1 MB", "compare_result": "111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

type MyHashSet struct {
	m map[int]struct{}
}

func Constructor() MyHashSet {
	return MyHashSet{map[int]struct{}{}}
}

func (this *MyHashSet) Add(key int) {
	this.m[key] = struct{}{}
}

func (this *MyHashSet) Remove(key int) {
	delete(this.m, key)
}

func (this *MyHashSet) Contains(key int) bool {
	_, ok := this.m[key]
	return ok
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
