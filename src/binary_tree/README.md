# Binary Tree Implementation

A Python implementation of a Binary Search Tree data structure, translated from the Go implementation.

## Structure

- `node.py` - Contains the `BinaryTreeNode` class with key attribute
- `test_binary_tree.py` - Unit tests for the binary tree implementation

## Features

- **Insert**: Add values to the binary tree maintaining BST property
- **Search**: Find if a value exists in the tree

## Usage

```python
from binary_tree import Node

# Create a new tree
tree = Node(data=100)

# Insert values
tree.insert(50)
tree.insert(150)
tree.insert(25)
tree.insert(75)

# Search for values
found = tree.search(50)  # Returns True
not_found = tree.search(200)  # Returns False
```

## Running Tests

```bash
pytest test_binary_tree.py
```

## Binary Search Tree Properties

- Left child node has a value less than the parent
- Right child node has a value greater than the parent
- No duplicate values are inserted
