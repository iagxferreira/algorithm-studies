package queue

import "fmt"

type Queue[T any] struct {
	items []T
}

func NewQueue[T any]() *Queue[T] {
	return &Queue[T]{
		items: make([]T, 0),
	}

}
func (queue *Queue[T]) Enqueue(item T) {
	queue.items = append(queue.items, item)
}

func (queue *Queue[T]) Dequeue() (T, bool) {
	var zero T
	if len(queue.items) == 0 {
		return zero, false
	}

	item := queue.items[0]
	queue.items = queue.items[1:]
	return item, true
}

func (queue *Queue[T]) Peek() (T, bool) {
	var zero T
	if len(queue.items) == 0 {
		return zero, false
	}

	return queue.items[0], true
}

func TestQueue() {
	queue := NewQueue[int]()
	queue.Enqueue(1)
	queue.Enqueue(2)

	item, _ := queue.Peek()
	fmt.Println(item)
}
