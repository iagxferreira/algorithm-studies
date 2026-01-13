package main

import (
	"fmt"
)

type Item[T any] struct {
	Value    T
	Priority int
}

type PriorityQueue[T any] struct {
	items []Item[T]
}

func NewPriorityQueue[T any]() *PriorityQueue[T] {
	return &PriorityQueue[T]{
		items: []Item[T]{},
	}
}

func (queue *PriorityQueue[T]) Enqueue(value T, priority int) {
	item := Item[T]{Value: value, Priority: priority}
	inserted := false

	for i, existing := range queue.items {
		if priority > existing.Priority {
			queue.items = append(queue.items, append([]Item[T]{item}, queue.items[i:]...)...)
			inserted = true
			break
		}
	}

	if !inserted {
		queue.items = append(queue.items, item)
	}
}

func (queue *PriorityQueue[T]) Dequeue() (T, bool) {
	var zero T
	if len(queue.items) == 0 {
		return zero, false
	}
	item := queue.items[0]
	queue.items = queue.items[1:]
	return item.Value, true
}

func (pq *PriorityQueue[T]) Peek() (T, bool) {
	var zero T
	if len(pq.items) == 0 {
		return zero, false
	}
	return pq.items[0].Value, true
}

func (pq *PriorityQueue[T]) Len() int {
	return len(pq.items)
}

func (pq *PriorityQueue[T]) IsEmpty() bool {
	return len(pq.items) == 0
}

func TestPriorityQueue() {
	q := NewPriorityQueue[string]()

	q.Enqueue("low", 1)
	q.Enqueue("medium", 5)
	q.Enqueue("high", 10)
	q.Enqueue("urgent", 100)

	for !q.IsEmpty() {
		val, _ := q.Dequeue()
		fmt.Println(val)
	}
}
