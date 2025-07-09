package main

import (
	"algorithm_studies/linked_list"
)

func main() {
	linkedList := linked_list.NewLinkedList()
	linkedList.Insert(10)
	linkedList.Insert(20)
	linkedList.Insert(40)
	linkedList.Insert(30)
	linkedList.Unshift(20)
	linkedList.Walk()
	linkedList.Show()
}
