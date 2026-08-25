class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __repr__(self):
        return f"Queue(front={self.front}, rear={self.rear}, size={self.size})"

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print(queue.dequeue())
    queue.display()
    print(queue.peek())
    print(queue.get_size())
    print(queue.is_empty())
