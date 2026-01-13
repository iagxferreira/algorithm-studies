package tree

import (
	"algorithm_studies/tree/node"
	"bytes"
	"encoding/json"
	"fmt"
)

type UnbalancedTree struct {
	Root   *node.TreeNode
	Depth  int
	Length int
}

func NewTree() *UnbalancedTree {
	return &UnbalancedTree{
		Root:   nil,
		Depth:  0,
		Length: 0,
	}
}

func AddLeaf(root *node.TreeNode, leaf *node.TreeNode) *node.TreeNode {
	if root == nil {
		return leaf
	}

	if root.Left == nil {
		root.Left = AddLeaf(root.Left, leaf)
		return root
	}

	root.Right = AddLeaf(root.Right, leaf)
	return root
}

func (tree *UnbalancedTree) Insert(data int) {
	node := node.NewTreeNode(data)
	tree.Root = AddLeaf(tree.Root, node)
}

func inOrder(node node.TreeNode) {
	inOrder(*node.Left)
	fmt.Println(node.Data)
	inOrder(*node.Right)
}

func (tree *UnbalancedTree) TraverseInOrder() {
	fmt.Println("in order")
	inOrder(*tree.Root)
}

func (tree *UnbalancedTree) Show() {
	serialized, _ := json.Marshal(tree)
	fmt.Println(string(serialized))
}

func (tree *UnbalancedTree) PrettyPrint() {
	var prettyJSON bytes.Buffer
	serialized, _ := json.Marshal(tree)
	_ = json.Indent(&prettyJSON, serialized, "", "\t")
	fmt.Println(string(prettyJSON.Bytes()))
}
