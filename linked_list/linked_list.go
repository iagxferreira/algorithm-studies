package main

import (
	"encoding/json"
	"fmt"
	"linked_list/node"
)

type LinkedList struct {
	Head *node.LinkedListNode
	Tail *node.LinkedListNode
}

func NewLinkedList() *LinkedList {
	return &LinkedList{
		Head: nil,
		Tail: nil,
	}
}

func (linkedList *LinkedList) Insert(data int32) {
	node := node.NewLinkedListNode(data)
	if linkedList.Head == nil {
		linkedList.Head = node
		linkedList.Tail = node
		return
	}

	linkedList.Tail.Next = node
	linkedList.Tail = node
}

func (linkedList *LinkedList) Unshift(data int32) {
	node := node.NewLinkedListNode(data)
	node.Next = linkedList.Head
	linkedList.Head = node
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
func main() {
	linkedList := NewLinkedList()
	linkedList.Insert(10)
	linkedList.Insert(20)
	linkedList.Insert(40)
	linkedList.Insert(30)
	linkedList.Unshift(20)
	linkedList.Walk()
	linkedList.Show()
}
