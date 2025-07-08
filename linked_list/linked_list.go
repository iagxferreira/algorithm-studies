package main

import "fmt"

type SinglyLinkedListNode struct {
	data int32
	next *SinglyLinkedListNode
}

type SinglyLinkedList struct {
	head *SinglyLinkedListNode
	tail *SinglyLinkedListNode
}

func (linkedList *SinglyLinkedList) Insert(data int32) {
	node := &SinglyLinkedListNode{
		next: nil,
		data: data,
	}
	if linkedList.head == nil {
		linkedList.head = node
	} else {
		linkedList.tail.next = node
	}

	linkedList.tail = node
}

func ReadNode(node *SinglyLinkedListNode) {
	fmt.Println(node.data)
	if node.next != nil {
		ReadNode(node.next)
	}
}
func (linkedList *SinglyLinkedList) Walk() {
	ReadNode(linkedList.head)
}

func main() {
	linkedList := SinglyLinkedList{}
	linkedList.Insert(10)
	linkedList.Insert(20)
	linkedList.Walk()
}
