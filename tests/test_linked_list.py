import os
import sys

import pytest

from linked_list.linked_list import LinkedList
from linked_list.node import ListNode


def test_init_with_no_head():
    """Test creating an empty linked list."""
    linked_list = LinkedList()
    assert linked_list.head is None


def test_init_with_head():
    """Test creating a linked list with an initial head node."""
    head_node = ListNode(1)
    linked_list = LinkedList(head_node)
    assert linked_list.head == head_node
    assert linked_list.head.value == 1


def test_add_to_single_node_list():
    """Test adding a node to a list with one node."""
    head_node = ListNode(1)
    linked_list = LinkedList(head_node)
    new_node = ListNode(2)

    linked_list.add(new_node)

    assert linked_list.head.next == new_node
    assert linked_list.head.next.value == 2


def test_add_multiple_nodes():
    """Test adding multiple nodes to the list."""
    head_node = ListNode(1)
    linked_list = LinkedList(head_node)

    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    linked_list.add(node2)
    linked_list.add(node3)
    linked_list.add(node4)

    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.head.next.next.next.value == 4
    assert linked_list.head.next.next.next.next is None


def test_add_maintains_order():
    """Test that add maintains the order of insertion."""
    head_node = ListNode(10)
    linked_list = LinkedList(head_node)

    values = [20, 30, 40, 50]
    for val in values:
        linked_list.add(ListNode(val))

    current = linked_list.head
    expected_values = [10, 20, 30, 40, 50]

    for expected_val in expected_values:
        assert current is not None
        assert current.value == expected_val
        current = current.next

    assert current is None


def test_add_with_different_data_types():
    """Test adding nodes with different value types."""
    head_node = ListNode("first")
    linked_list = LinkedList(head_node)

    linked_list.add(ListNode(42))
    linked_list.add(ListNode(3.14))
    linked_list.add(ListNode(True))

    assert linked_list.head.value == "first"
    assert linked_list.head.next.value == 42
    assert linked_list.head.next.next.value == 3.14
    assert linked_list.head.next.next.next.value is True


def test_add_to_empty_list_raises_error():
    """Test that adding to an empty list (no head) raises an AttributeError."""
    linked_list = LinkedList()
    new_node = ListNode(1)

    with pytest.raises(AttributeError):
        linked_list.add(new_node)
