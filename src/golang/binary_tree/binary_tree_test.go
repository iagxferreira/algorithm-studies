package binary_tree_test

import (
	"binary_tree"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestInsertNode(t *testing.T) {
	tree := binary_tree.Node{
		Key: 100,
	}
	tree.Insert(200)
	assert.Equal(t, tree.Right.Key, 200, "Right value should be 200")
}

func TestSearchNode(t *testing.T) {
	tree := binary_tree.Node{
		Key: 100,
	}
	tree.Insert(200)
	assert.Equal(t, tree.Search(200), true, "Value 200 should be found")
}
