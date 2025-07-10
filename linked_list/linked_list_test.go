package linked_list_test

import (
	"algorithm_studies/linked_list"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInsert(t *testing.T) {
	linkedList := linked_list.NewLinkedList()
	linkedList.Insert(10)
	assert.Equal(t, linkedList.Head.Data, 10, "Data value should be 10")
}

func TestUnshift(t *testing.T) {
	linkedList := linked_list.NewLinkedList()
	linkedList.Insert(10)
	linkedList.Unshift(20)
	assert.Equal(t, linkedList.Head.Data, 20, "Data value should be 20")
}

func TestReverse(t *testing.T) {
	linkedList := linked_list.NewLinkedList()
	linkedList.Insert(1)
	linkedList.Insert(2)
	linkedList.Insert(3)

	mockLinkedList := linked_list.NewLinkedList()
	mockLinkedList.Insert(3)
	mockLinkedList.Insert(2)
	mockLinkedList.Insert(1)

	assert.Equal(t, linkedList.Reverse().Show(), mockLinkedList.Show())
}
