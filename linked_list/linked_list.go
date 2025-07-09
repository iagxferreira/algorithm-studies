package linked_list

import (
	"algorithm_studies/linked_list/node"
	"encoding/json"
	"fmt"
)

type LinkedList struct {
	Head   *node.LinkedListNode
	Tail   *node.LinkedListNode
	Length int
}

func NewLinkedList() *LinkedList {
	return &LinkedList{
		Head:   nil,
		Tail:   nil,
		Length: 0,
	}
}

func (linkedList *LinkedList) Insert(data int) {
	node := node.NewLinkedListNode(data)
	if linkedList.Head == nil {
		linkedList.Head = node
		linkedList.Tail = node
		linkedList.Length = 1
		return
	}

	linkedList.Tail.Next = node
	linkedList.Tail = node
	linkedList.Length += 1
}

func (linkedList *LinkedList) Unshift(data int) {
	node := node.NewLinkedListNode(data)
	node.Next = linkedList.Head
	linkedList.Head = node
	linkedList.Length += 1
}

func (linkedList *LinkedList) Walk() {
	node := linkedList.Head
	for node != nil {
		fmt.Println(node.Data)
		node = node.Next
	}
}

func (linkedList *LinkedList) Show() {
	serialized, _ := json.Marshal(linkedList)
	fmt.Println(string(serialized))
}
