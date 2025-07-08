package main

import (
	"encoding/json"
	"fmt"
)

type Node struct {
	Key   int
	Left  *Node
	Right *Node
}

func (node *Node) Insert(value int) {
	if node.Key < value {
		if node.Right == nil {
			node.Right = &Node{Key: value}
		} else {
			node.Right.Insert(value)
		}
	} else if node.Key > value {
		if node.Left == nil {
			node.Left = &Node{Key: value}
		} else {
			node.Left.Insert(value)
		}
	}
}

func (node *Node) Search(value int) bool {
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

func main() {
	tree := &Node{Key: 100}
	tree.Insert(200)
	tree.Insert(300)
	out, _ := json.Marshal(tree)
	fmt.Println(string(out))
	fmt.Println(tree.Search(400))
}
