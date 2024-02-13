// Submission title: Construct Quad Tree
// Submission url  : https://leetcode.com/problems/construct-quad-tree/description/
// Submission url  : https://leetcode.com/submissions/detail/1091201489/
// Submission json : {"id":1091201489,"status_display":"Accepted","lang":"golang","question_id":772,"title_slug":"construct-quad-tree","code":"/**\n * Definition for a QuadTree node.\n * type Node struct {\n *     Val bool\n *     IsLeaf bool\n *     TopLeft *Node\n *     TopRight *Node\n *     BottomLeft *Node\n *     BottomRight *Node\n * }\n */\n\nfunc construct(grid [][]int) *Node {\n\tvar dfs func(y0, x0, width int) *Node\n\tdfs = func(y0, x0, width int) *Node {\n\t\tif width == 1 {\n\t\t\treturn &Node{\n\t\t\t\tVal:    grid[y0][x0] == 1,\n\t\t\t\tIsLeaf: true,\n\t\t\t}\n\t\t}\n\n\t\tw := width / 2\n\t\ttopLeft := dfs(y0, x0, w)\n\t\ttopRight := dfs(y0, x0+w, w)\n\t\tbottomLeft := dfs(y0+w, x0, w)\n\t\tbottomRight := dfs(y0+w, x0+w, w)\n\t\tvar node *Node\n\n\t\tif topLeft.Val == topRight.Val && bottomLeft.Val == bottomRight.Val && topLeft.Val == bottomLeft.Val &&\n\t\t\ttopLeft.IsLeaf && topRight.IsLeaf && bottomLeft.IsLeaf && bottomRight.IsLeaf {\n\t\t\tnode = &Node{\n\t\t\t\tVal:    topLeft.Val,\n\t\t\t\tIsLeaf: true,\n\t\t\t}\n\t\t} else {\n\t\t\tnode = &Node{\n\t\t\t\tVal:         true,\n\t\t\t\tIsLeaf:      false,\n\t\t\t\tTopLeft:     topLeft,\n\t\t\t\tTopRight:    topRight,\n\t\t\t\tBottomLeft:  bottomLeft,\n\t\t\t\tBottomRight: bottomRight,\n\t\t\t}\n\t\t}\n\t\treturn node\n\t}\n\treturn dfs(0, 0, len(grid))\n}\n","title":"Construct Quad Tree","url":"/submissions/detail/1091201489/","lang_name":"Go","time":"3 months","timestamp":1699093791,"status":10,"runtime":"10 ms","is_pending":"Not Pending","memory":"6.6 MB","compare_result":"1111111111111111111111","has_notes":false,"flag_type":1}
package submissions

/**
 * Definition for a QuadTree node.
 * type Node struct {
 *     Val bool
 *     IsLeaf bool
 *     TopLeft *Node
 *     TopRight *Node
 *     BottomLeft *Node
 *     BottomRight *Node
 * }
 */

func construct(grid [][]int) *Node {
	var dfs func(y0, x0, width int) *Node
	dfs = func(y0, x0, width int) *Node {
		if width == 1 {
			return &Node{
				Val:    grid[y0][x0] == 1,
				IsLeaf: true,
			}
		}

		w := width / 2
		topLeft := dfs(y0, x0, w)
		topRight := dfs(y0, x0+w, w)
		bottomLeft := dfs(y0+w, x0, w)
		bottomRight := dfs(y0+w, x0+w, w)
		var node *Node

		if topLeft.Val == topRight.Val && bottomLeft.Val == bottomRight.Val && topLeft.Val == bottomLeft.Val &&
			topLeft.IsLeaf && topRight.IsLeaf && bottomLeft.IsLeaf && bottomRight.IsLeaf {
			node = &Node{
				Val:    topLeft.Val,
				IsLeaf: true,
			}
		} else {
			node = &Node{
				Val:         true,
				IsLeaf:      false,
				TopLeft:     topLeft,
				TopRight:    topRight,
				BottomLeft:  bottomLeft,
				BottomRight: bottomRight,
			}
		}
		return node
	}
	return dfs(0, 0, len(grid))
}
