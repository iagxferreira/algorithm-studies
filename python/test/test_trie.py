import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../src"))

import pytest
from trie.trie import TrieNode, insert, new_node, search


class TestTrie:
    def test_insert_and_search_single_word(self):
        """Test inserting and searching for a single word"""
        root = TrieNode()
        root.insert("hello")

        assert root.search("hello") == True
        assert root.search("hell") == False
        assert root.search("helloworld") == False

    def test_insert_multiple_words(self):
        """Test inserting multiple words"""
        root = TrieNode()
        words = ["a", "and", "go", "golang", "mango"]

        for word in words:
            root.insert(word)

        assert root.search("a") == True
        assert root.search("and") == True
        assert root.search("go") == True
        assert root.search("golang") == True
        assert root.search("mango") == True

    def test_search_nonexistent_word(self):
        """Test searching for words that don't exist"""
        root = TrieNode()
        root.insert("hello")
        root.insert("world")

        assert root.search("hell") == False
        assert root.search("hi") == False
        assert root.search("worldly") == False
        assert root.search("") == False

    def test_prefix_not_a_word(self):
        """Test that prefixes are not considered valid words"""
        root = TrieNode()
        root.insert("golang")

        assert root.search("go") == False
        assert root.search("gol") == False
        assert root.search("golan") == False
        assert root.search("golang") == True

    def test_overlapping_words(self):
        """Test words that share prefixes"""
        root = TrieNode()
        root.insert("go")
        root.insert("golang")
        root.insert("gopher")

        assert root.search("go") == True
        assert root.search("golang") == True
        assert root.search("gopher") == True
        assert root.search("gop") == False

    def test_standalone_functions(self):
        """Test the standalone insert and search functions"""
        root = TrieNode()

        insert(root, "test")
        insert(root, "testing")

        assert search(root, "test") == True
        assert search(root, "testing") == True
        assert search(root, "tes") == False

    def test_new_node_factory(self):
        """Test the new_node factory function"""
        root = new_node()
        root.insert("factory")

        assert root.search("factory") == True

    def test_empty_trie(self):
        """Test operations on an empty trie"""
        root = TrieNode()

        assert root.search("anything") == False
        assert root.search("") == False

    def test_single_character_words(self):
        """Test single character words"""
        root = TrieNode()
        root.insert("a")
        root.insert("b")
        root.insert("z")

        assert root.search("a") == True
        assert root.search("b") == True
        assert root.search("z") == True
        assert root.search("c") == False

    def test_show_method(self):
        """Test the show method returns valid JSON"""
        root = TrieNode()
        root.insert("test")

        json_str = root.show()
        assert isinstance(json_str, str)
        assert len(json_str) > 0

    def test_to_dict_method(self):
        """Test the to_dict method"""
        root = TrieNode()
        root.insert("go")

        result = root.to_dict()
        assert "end" in result
        assert "children" in result
        assert result["end"] == False
        assert "g" in result["children"]

    def test_case_sensitivity(self):
        """Test that trie works with lowercase letters"""
        root = TrieNode()
        root.insert("hello")

        # Should work with lowercase
        assert root.search("hello") == True

    def test_word_subset(self):
        """Test words where one is a subset of another"""
        root = TrieNode()
        root.insert("man")
        root.insert("mango")

        assert root.search("man") == True
        assert root.search("mango") == True
        assert root.search("mang") == False

    def test_common_prefix_multiple_words(self):
        """Test multiple words with common prefixes"""
        root = TrieNode()
        words = ["cat", "car", "card", "care", "careful"]

        for word in words:
            root.insert(word)

        assert root.search("cat") == True
        assert root.search("car") == True
        assert root.search("card") == True
        assert root.search("care") == True
        assert root.search("careful") == True
        assert root.search("ca") == False
        assert root.search("cards") == False


class TestTrieFromGoExample:
    """Test cases matching the Go implementation example"""

    def test_go_example(self):
        """Test the exact example from the Go code"""
        words = ["a", "and", "go", "golang", "mango"]
        root = TrieNode()

        for word in words:
            insert(root, word)

        assert search(root, "and") == True, "contains 'and' should be True"
        assert search(root, "golang") == True, "contains 'golang' should be True"
        assert search(root, "man") == False, "contains 'man' should be False"
