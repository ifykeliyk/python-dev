class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    def pop(self):
        if self.head is None:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(10)
linked_list.display()
print(linked_list.pop())
linked_list.display()
print(linked_list.contains(40))
print(linked_list.length())
