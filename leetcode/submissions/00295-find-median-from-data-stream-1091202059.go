// Submission title: Find Median from Data Stream
// Submission url  : https://leetcode.com/problems/find-median-from-data-stream/description/
// Submission url  : https://leetcode.com/submissions/detail/1091202059/
// Submission json : {"id":1091202059,"status_display":"Accepted","lang":"golang","question_id":295,"title_slug":"find-median-from-data-stream","code":"type MaxHeap []int\nfunc (m MaxHeap) Len() int { return len(m) }\nfunc (m MaxHeap) Less(i, j int) bool { return m[i] > m[j] }\nfunc (m MaxHeap) Swap(i, j int) { m[i], m[j] = m[j], m[i] }\nfunc (m *MaxHeap) Pop() interface{} {\n    v := (*m)[len(*m)-1]\n    *m = (*m)[:len(*m)-1]\n    return v\n}\nfunc (m *MaxHeap) Push(v interface{}) { *m = append(*m, v.(int)) }\nfunc (m MaxHeap) Top() int { return m[0] }\n\ntype MinHeap []int\nfunc (m MinHeap) Len() int { return len(m) }\nfunc (m MinHeap) Less(i, j int) bool { return m[i] < m[j] }\nfunc (m MinHeap) Swap(i, j int) { m[i], m[j] = m[j], m[i] }\nfunc (m *MinHeap) Pop() interface{} {\n    v := (*m)[len(*m)-1]\n    *m = (*m)[:len(*m)-1]\n    return v\n}\nfunc (m *MinHeap) Push(v interface{}) { *m = append(*m, v.(int)) }\nfunc (m MinHeap) Top() int { return m[0] }\n\ntype MedianFinder struct {\n    left MaxHeap\n    right MinHeap    \n}\n\nfunc Constructor() MedianFinder {\n    return MedianFinder{}    \n}\n\nfunc (mf *MedianFinder) AddNum(num int)  {\n    if len(mf.left) + len(mf.right) == 0 {\n        heap.Push(&(mf.left), num)\n        return\n    }\n    for {\n        if len(mf.left) < len(mf.right) {\n            if num <= mf.right.Top() {\n                heap.Push(&(mf.left), num)\n                return\n            } else {\n                v := heap.Pop(&(mf.right))\n                heap.Push(&(mf.left), v)\n            }\n        } else {\n            if num >= mf.left.Top() {\n                heap.Push(&(mf.right), num)\n                return\n            } else {\n                v := heap.Pop(&(mf.left))\n                heap.Push(&(mf.right), v)\n            }\n        }\n    }\n}\n\nfunc (mf *MedianFinder) FindMedian() float64 {\n    if len(mf.left) == len(mf.right) {\n        return float64(mf.left.Top() + mf.right.Top()) / 2.0\n    } else if len(mf.left) > len(mf.right) {\n        return float64(mf.left.Top())\n    } else {\n        return float64(mf.right.Top())\n    }   \n}","title":"Find Median from Data Stream","url":"/submissions/detail/1091202059/","lang_name":"Go","time":"3 months","timestamp":1699093864,"status":10,"runtime":"299 ms","is_pending":"Not Pending","memory":"20.2 MB","compare_result":"111111111111111111111","has_notes":false,"flag_type":1}
package submissions

type MaxHeap []int

func (m MaxHeap) Len() int           { return len(m) }
func (m MaxHeap) Less(i, j int) bool { return m[i] > m[j] }
func (m MaxHeap) Swap(i, j int)      { m[i], m[j] = m[j], m[i] }
func (m *MaxHeap) Pop() interface{} {
	v := (*m)[len(*m)-1]
	*m = (*m)[:len(*m)-1]
	return v
}
func (m *MaxHeap) Push(v interface{}) { *m = append(*m, v.(int)) }
func (m MaxHeap) Top() int            { return m[0] }

type MinHeap []int

func (m MinHeap) Len() int           { return len(m) }
func (m MinHeap) Less(i, j int) bool { return m[i] < m[j] }
func (m MinHeap) Swap(i, j int)      { m[i], m[j] = m[j], m[i] }
func (m *MinHeap) Pop() interface{} {
	v := (*m)[len(*m)-1]
	*m = (*m)[:len(*m)-1]
	return v
}
func (m *MinHeap) Push(v interface{}) { *m = append(*m, v.(int)) }
func (m MinHeap) Top() int            { return m[0] }

type MedianFinder struct {
	left  MaxHeap
	right MinHeap
}

func Constructor() MedianFinder {
	return MedianFinder{}
}

func (mf *MedianFinder) AddNum(num int) {
	if len(mf.left)+len(mf.right) == 0 {
		heap.Push(&(mf.left), num)
		return
	}
	for {
		if len(mf.left) < len(mf.right) {
			if num <= mf.right.Top() {
				heap.Push(&(mf.left), num)
				return
			} else {
				v := heap.Pop(&(mf.right))
				heap.Push(&(mf.left), v)
			}
		} else {
			if num >= mf.left.Top() {
				heap.Push(&(mf.right), num)
				return
			} else {
				v := heap.Pop(&(mf.left))
				heap.Push(&(mf.right), v)
			}
		}
	}
}

func (mf *MedianFinder) FindMedian() float64 {
	if len(mf.left) == len(mf.right) {
		return float64(mf.left.Top()+mf.right.Top()) / 2.0
	} else if len(mf.left) > len(mf.right) {
		return float64(mf.left.Top())
	} else {
		return float64(mf.right.Top())
	}
}
