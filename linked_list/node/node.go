package node

type LinkedListNode struct {
	Data int32
	Next *LinkedListNode
}

func NewLinkedListNode(data int32) *LinkedListNode {
	return &LinkedListNode{
		Data: data,
		Next: nil,
	}
}
