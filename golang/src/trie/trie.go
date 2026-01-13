package trie

import (
	"bytes"
	"encoding/json"
	"fmt"
)

const ALPHABET_SIZE = 26

type TrieNode struct {
	Children [ALPHABET_SIZE]*TrieNode
	End      bool
}

func NewNode() *TrieNode {
	node := &TrieNode{
		End: false,
	}

	for i := 0; i < ALPHABET_SIZE; i++ {
		node.Children[i] = nil
	}

	return node

}

func Insert(root *TrieNode, key string) {
	temp := root
	for i := 0; i < len(key); i++ {
		index := key[i] - 'a'
		if temp.Children[index] == nil {
			temp.Children[index] = NewNode()
		}
		temp = temp.Children[index]
	}
	temp.End = true
}

func Search(root *TrieNode, key string) bool {
	temp := root
	for i := 0; i < len(key); i++ {
		index := key[i] - 'a'
		if temp.Children[index] != nil {
			temp = temp.Children[index]
		} else {
			return false
		}
	}
	return (temp != nil && temp.End)
}

func (trie *TrieNode) Show() string {
	serialized, _ := json.Marshal(trie)
	fmt.Println(string(serialized))
	return string(serialized)
}

func (trie *TrieNode) PrettyPrint() {
	var prettyJSON bytes.Buffer
	serialized, _ := json.Marshal(trie)
	_ = json.Indent(&prettyJSON, serialized, "", "\t")
	fmt.Println(string(prettyJSON.Bytes()))
}

func TestTrie() {
	words := []string{"a", "and", "go", "golang", "mango"}
	root := NewNode()
	for _, value := range words {
		Insert(root, value)
	}

	fmt.Println("contains and", Search(root, "and"))
	fmt.Println("contains golang", Search(root, "golang"))
	fmt.Println("contains man", Search(root, "man"))
	root.PrettyPrint()
}
