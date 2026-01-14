import json
from typing import List, Optional

ALPHABET_SIZE = 26


class TrieNode:
    """Trie node for storing words efficiently"""

    def __init__(self):
        self.children: List[Optional["TrieNode"]] = [None] * ALPHABET_SIZE
        self.end: bool = False

    def insert(self, key: str) -> None:
        """
        Insert a word into the trie.
        Assumes lowercase letters only (a-z).
        """
        temp = self
        for char in key:
            index = ord(char) - ord("a")
            if temp.children[index] is None:
                temp.children[index] = TrieNode()
            temp = temp.children[index]
        temp.end = True

    def search(self, key: str) -> bool:
        """
        Search for a word in the trie.
        Returns True if the word exists, False otherwise.
        """
        temp = self
        for char in key:
            index = ord(char) - ord("a")
            if temp.children[index] is not None:
                temp = temp.children[index]
            else:
                return False
        return temp is not None and temp.end

    def to_dict(self) -> dict:
        """Convert trie to dictionary for JSON serialization"""
        result = {"end": self.end, "children": {}}
        for i, child in enumerate(self.children):
            if child is not None:
                char = chr(ord("a") + i)
                result["children"][char] = child.to_dict()
        return result

    def show(self) -> str:
        """Return JSON representation of the trie"""
        data = self.to_dict()
        json_str = json.dumps(data)
        print(json_str)
        return json_str

    def pretty_print(self) -> None:
        """Print a formatted JSON representation of the trie"""
        data = self.to_dict()
        pretty_json = json.dumps(data, indent=4)
        print(pretty_json)


def new_node() -> TrieNode:
    """Factory function to create a new trie node"""
    return TrieNode()


def insert(root: TrieNode, key: str) -> None:
    """Insert a word into the trie (standalone function)"""
    root.insert(key)


def search(root: TrieNode, key: str) -> bool:
    """Search for a word in the trie (standalone function)"""
    return root.search(key)


def test_trie():
    """Test the trie implementation"""
    words = ["a", "and", "go", "golang", "mango"]
    root = TrieNode()

    for word in words:
        insert(root, word)

    print(f"contains 'and': {search(root, 'and')}")
    print(f"contains 'golang': {search(root, 'golang')}")
    print(f"contains 'man': {search(root, 'man')}")
    print("\nTrie structure:")
    root.pretty_print()


if __name__ == "__main__":
    test_trie()
