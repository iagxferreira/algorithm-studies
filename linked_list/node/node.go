package node

type LinkedListNode struct {
	Data int
	Next *LinkedListNode
}

func NewLinkedListNode(data int) *LinkedListNode {
	return &LinkedListNode{
		Data: data,
		Next: nil,
	}
}
