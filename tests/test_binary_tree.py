import os
import sys

import pytest

from binary_tree.binary_tree_node import BinaryTreeNode


def test_insert_node():
    """Test inserting a node into the binary tree"""
    tree = BinaryTreeNode(key=100)
    tree.insert(200)
    assert tree.right.key == 200, "Right value should be 200"


def test_search_node():
    """Test searching for a value in the binary tree"""
    tree = BinaryTreeNode(key=100)
    tree.insert(200)
    assert tree.search(200) == True, "Value 200 should be found"


def test_search_missing_node():
    """Test searching for a value that doesn't exist"""
    tree = BinaryTreeNode(key=100)
    tree.insert(200)
    assert tree.search(150) == False, "Value 150 should not be found"


def test_insert_multiple_values():
    """Test inserting multiple values"""
    tree = BinaryTreeNode(key=100)
    tree.insert(50)
    tree.insert(150)
    tree.insert(25)
    tree.insert(75)

    assert tree.left.key == 50, "Left child should be 50"
    assert tree.right.key == 150, "Right child should be 150"
    assert tree.left.left.key == 25, "Left-left child should be 25"
    assert tree.left.right.key == 75, "Left-right child should be 75"


def test_search_in_complex_tree():
    """Test searching in a tree with multiple nodes"""
    tree = BinaryTreeNode(key=100)
    tree.insert(50)
    tree.insert(150)
    tree.insert(25)
    tree.insert(75)
    tree.insert(125)
    tree.insert(175)

    assert tree.search(25) == True
    assert tree.search(75) == True
    assert tree.search(125) == True
    assert tree.search(175) == True
    assert tree.search(200) == False
    assert tree.search(10) == False
