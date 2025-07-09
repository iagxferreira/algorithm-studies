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
