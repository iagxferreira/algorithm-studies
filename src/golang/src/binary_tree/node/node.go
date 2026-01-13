package node

type BinaryTreeNode struct {
	Key   int
	Left  *BinaryTreeNode
	Right *BinaryTreeNode
}

func (node BinaryTreeNode) Insert(value int) {
	if node.Key < value {
		if node.Right == nil {
			node.Right = &BinaryTreeNode{Key: value}
		} else {
			node.Right.Insert(value)
		}
	} else if node.Key > value {
		if node.Left == nil {
			node.Left = &BinaryTreeNode{Key: value}
		} else {
			node.Left.Insert(value)
		}
	}
}

func (node *BinaryTreeNode) Search(value int) bool {
	if node == nil {
		return false
	}
	if node.Key < value {
		return node.Right.Search(value)
	} else if node.Key > value {
		return node.Left.Search(value)
	}
	return true
}
