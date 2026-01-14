from dataclasses import dataclass
from typing import Generic, Optional, Tuple, TypeVar

T = TypeVar("T")


@dataclass
class Item(Generic[T]):
    """Item with a value and priority"""

    value: T
    priority: int


class PriorityQueue(Generic[T]):
    """Priority Queue implementation where higher priority items are dequeued first"""

    def __init__(self):
        self.items: list[Item[T]] = []

    def enqueue(self, value: T, priority: int) -> None:
        """
        Add an item to the queue with a given priority.
        Higher priority items are placed before lower priority items.
        """
        item = Item(value=value, priority=priority)
        inserted = False

        for i, existing in enumerate(self.items):
            if priority > existing.priority:
                self.items.insert(i, item)
                inserted = True
                break

        if not inserted:
            self.items.append(item)

    def dequeue(self) -> Tuple[Optional[T], bool]:
        """
        Remove and return the highest priority item.
        Returns (value, True) if successful, (None, False) if empty.
        """
        if len(self.items) == 0:
            return None, False

        item = self.items.pop(0)
        return item.value, True

    def peek(self) -> Tuple[Optional[T], bool]:
        """
        Return the highest priority item without removing it.
        Returns (value, True) if successful, (None, False) if empty.
        """
        if len(self.items) == 0:
            return None, False

        return self.items[0].value, True

    def __len__(self) -> int:
        """Return the number of items in the queue"""
        return len(self.items)

    def is_empty(self) -> bool:
        """Check if the queue is empty"""
        return len(self.items) == 0


def test_priority_queue():
    """Test the priority queue implementation"""
    q = PriorityQueue[str]()

    q.enqueue("low", 1)
    q.enqueue("medium", 5)
    q.enqueue("high", 10)
    q.enqueue("urgent", 100)

    while not q.is_empty():
        val, _ = q.dequeue()
        print(val)


if __name__ == "__main__":
    test_priority_queue()
