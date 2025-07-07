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
func main() {
	tree := &Node{Key: 100}
	tree.Insert(50)
	fmt.Println(tree)
	fmt.Println(tree.Left)
	out, _ := json.Marshal(tree)
	fmt.Println(string(out))

}
