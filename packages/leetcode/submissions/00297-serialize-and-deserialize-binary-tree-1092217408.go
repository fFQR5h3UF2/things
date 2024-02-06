// Submission title: for Serialize and Deserialize Binary Tree
// Submission url  : https://leetcode.com/submissions/detail/1092217408/
// Submission json : {"id": 1092217408, "status_display": "Accepted", "lang": "golang", "question_id": 297, "title_slug": "serialize-and-deserialize-binary-tree", "code": "/**\n * Definition for a binary tree node.\n * type TreeNode struct {\n *     Val int\n *     Left *TreeNode\n *     Right *TreeNode\n * }\n */\n\ntype Codec struct {\n    \n}\n\nfunc Constructor() Codec {\n    return Codec{}\n}\n\n// Serializes a tree to a single string.\nfunc (this *Codec) serialize(root *TreeNode) string {\n    if root == nil {\n        return \"\"\n    }\n    var buffer bytes.Buffer\n    queue := []*TreeNode{root}\n    for length := len(queue); length > 0; length = len(queue) {\n        for i := 0; i < length; i++ {\n            node := queue[i]\n            if node != nil {\n                buffer.WriteString(strconv.Itoa(node.Val))\n                queue = append(queue, node.Left, node.Right)\n            }\n            buffer.WriteString(\",\")\n        }\n        queue = queue[length:]\n    }\n    ans := buffer.String()\n    return ans[:len(ans)-1]\n}\n\n// Deserializes your encoded data to tree.\nfunc (this *Codec) deserialize(data string) *TreeNode {    \n    nodes := []*TreeNode{}\n    for _, str := range strings.Split(data, \",\") {\n        if str == \"\" {\n            nodes = append(nodes, nil)\n        } else {\n            num, _ := strconv.Atoi(str)\n            nodes = append(nodes, &TreeNode{num, nil, nil})\n        }\n    }\n    start := 0\n    length := len(nodes)\n    for _, node := range nodes {\n        if node == nil {\n            continue\n        }\n        left, right := 2 * start + 1, 2 * start + 2\n        if left < length {\n            node.Left = nodes[left]\n        }\n        if right < length {\n            node.Right = nodes[right]\n        }\n        start++\n    }\n    return nodes[0]\n}\n\n\n/**\n * Your Codec object will be instantiated and called as such:\n * ser := Constructor();\n * deser := Constructor();\n * data := ser.serialize(root);\n * ans := deser.deserialize(data);\n */", "title": "Serialize and Deserialize Binary Tree", "url": "/submissions/detail/1092217408/", "lang_name": "Go", "time": "3\u00a0months", "timestamp": 1699207360, "status": 10, "runtime": "11 ms", "is_pending": "Not Pending", "memory": "7.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}

package submissions

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Serializes a tree to a single string.
func (this *Codec) serialize(root *TreeNode) string {
	if root == nil {
		return ""
	}
	var buffer bytes.Buffer
	queue := []*TreeNode{root}
	for length := len(queue); length > 0; length = len(queue) {
		for i := 0; i < length; i++ {
			node := queue[i]
			if node != nil {
				buffer.WriteString(strconv.Itoa(node.Val))
				queue = append(queue, node.Left, node.Right)
			}
			buffer.WriteString(",")
		}
		queue = queue[length:]
	}
	ans := buffer.String()
	return ans[:len(ans)-1]
}

// Deserializes your encoded data to tree.
func (this *Codec) deserialize(data string) *TreeNode {
	nodes := []*TreeNode{}
	for _, str := range strings.Split(data, ",") {
		if str == "" {
			nodes = append(nodes, nil)
		} else {
			num, _ := strconv.Atoi(str)
			nodes = append(nodes, &TreeNode{num, nil, nil})
		}
	}
	start := 0
	length := len(nodes)
	for _, node := range nodes {
		if node == nil {
			continue
		}
		left, right := 2*start+1, 2*start+2
		if left < length {
			node.Left = nodes[left]
		}
		if right < length {
			node.Right = nodes[right]
		}
		start++
	}
	return nodes[0]
}

/**
 * Your Codec object will be instantiated and called as such:
 * ser := Constructor();
 * deser := Constructor();
 * data := ser.serialize(root);
 * ans := deser.deserialize(data);
 */
