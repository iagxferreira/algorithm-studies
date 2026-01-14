import os
import sys
from queue.priority_queue import PriorityQueue

import pytest


def test_enqueue_and_dequeue():
    """Test basic enqueue and dequeue operations"""
    q = PriorityQueue[str]()

    q.enqueue("low", 1)
    q.enqueue("high", 10)

    val, success = q.dequeue()
    assert success == True
    assert val == "high"

    val, success = q.dequeue()
    assert success == True
    assert val == "low"


def test_dequeue_empty_queue():
    """Test dequeuing from an empty queue"""
    q = PriorityQueue[str]()

    val, success = q.dequeue()
    assert success == False
    assert val is None


def test_priority_ordering():
    """Test that items are dequeued in priority order"""
    q = PriorityQueue[str]()

    q.enqueue("low", 1)
    q.enqueue("medium", 5)
    q.enqueue("high", 10)
    q.enqueue("urgent", 100)

    expected_order = ["urgent", "high", "medium", "low"]
    actual_order = []

    while not q.is_empty():
        val, _ = q.dequeue()
        actual_order.append(val)

    assert actual_order == expected_order


def test_same_priority():
    """Test items with the same priority maintain FIFO order"""
    q = PriorityQueue[str]()

    q.enqueue("first", 5)
    q.enqueue("second", 5)
    q.enqueue("third", 5)

    val1, _ = q.dequeue()
    val2, _ = q.dequeue()
    val3, _ = q.dequeue()

    assert val1 == "first"
    assert val2 == "second"
    assert val3 == "third"


def test_peek():
    """Test peek operation doesn't remove item"""
    q = PriorityQueue[str]()

    q.enqueue("low", 1)
    q.enqueue("high", 10)

    val, success = q.peek()
    assert success == True
    assert val == "high"

    # Queue should still have 2 items
    assert len(q) == 2


def test_peek_empty_queue():
    """Test peeking at an empty queue"""
    q = PriorityQueue[str]()

    val, success = q.peek()
    assert success == False
    assert val is None


def test_len():
    """Test length method"""
    q = PriorityQueue[int]()

    assert len(q) == 0

    q.enqueue(1, 1)
    assert len(q) == 1

    q.enqueue(2, 2)
    assert len(q) == 2

    q.dequeue()
    assert len(q) == 1


def test_is_empty():
    """Test is_empty method"""
    q = PriorityQueue[int]()

    assert q.is_empty() == True

    q.enqueue(1, 1)
    assert q.is_empty() == False

    q.dequeue()
    assert q.is_empty() == True


def test_mixed_priorities():
    """Test inserting items with mixed priorities"""
    q = PriorityQueue[str]()

    q.enqueue("p5", 5)
    q.enqueue("p10", 10)
    q.enqueue("p1", 1)
    q.enqueue("p7", 7)
    q.enqueue("p3", 3)

    expected = ["p10", "p7", "p5", "p3", "p1"]
    actual = []

    while not q.is_empty():
        val, _ = q.dequeue()
        actual.append(val)

    assert actual == expected


def test_different_types():
    """Test priority queue with different value types"""
    q = PriorityQueue[int]()

    q.enqueue(100, 1)
    q.enqueue(200, 10)
    q.enqueue(300, 5)

    val, _ = q.dequeue()
    assert val == 200
