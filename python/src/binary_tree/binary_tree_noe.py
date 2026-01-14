class BinaryTreeNode:
    """Binary Tree Node implementation"""

    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value: int) -> None:
        """Insert a value into the binary tree"""
        if self.key < value:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)
        elif self.key > value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)

    def search(self, value: int) -> bool:
        """Search for a value in the binary tree"""
        if self.key < value:
            if self.right is None:
                return False
            return self.right.search(value)
        elif self.key > value:
            if self.left is None:
                return False
            return self.left.search(value)
        return True
