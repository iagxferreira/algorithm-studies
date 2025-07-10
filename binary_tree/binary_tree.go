package binary_tree

type Node struct {
	Data  int
	Right *Node
	Left  *Node
}

func NewNode(data int) *Node {
	return &Node{
		Data: data,
	}
}
func (node *Node) Insert(value int) {
	if node.Data < value {
		if node.Right == nil {
			node.Right = &Node{Data: value}
		} else {
			node.Right.Insert(value)
		}
	} else if node.Data > value {
		if node.Left == nil {
			node.Left = &Node{Data: value}
		} else {
			node.Left.Insert(value)
		}
	}
}

func (node *Node) Search(value int) bool {
	if node == nil {
		return false
	}
	if node.Data < value {
		return node.Right.Search(value)
	} else if node.Data > value {
		return node.Left.Search(value)
	}
	return true
}
