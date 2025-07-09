package main

import (
	"algorithm_studies/tree"
)

func main() {
	tree := tree.NewTree()
	tree.Insert(10)
	tree.Insert(50)
	tree.Insert(30)
	tree.Insert(40)
	tree.Insert(20)
	tree.Insert(700)
	tree.Insert(600)
	tree.Insert(500)
	tree.PrettyPrint()
}
