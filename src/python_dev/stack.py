class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __repr__(self):
        return f"Stack(top={self.top}, size={self.size})"

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print(stack.pop())
    stack.display()
    print(stack.peek())
    print(stack.get_size())
    print(stack.is_empty())
