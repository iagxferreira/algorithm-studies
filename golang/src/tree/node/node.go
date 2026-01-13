package node

type TreeNode struct {
	Data  int
	Right *TreeNode
	Left  *TreeNode
}

func NewTreeNode(data int) *TreeNode {
	return &TreeNode{
		Data:  data,
		Left:  nil,
		Right: nil,
	}
}
func (node *TreeNode) Insert(data *TreeNode) {

	while
	if node.Right == nil {
		node.Right = data
		return
	} else if node.Left == nil {
		node.Left = data
		return
	} else {

		node.Right.Insert(data)
		node.Left.Insert(data)
	}

}
