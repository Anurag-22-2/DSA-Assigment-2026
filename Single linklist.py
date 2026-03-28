class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_value(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



sll = SinglyLinkedList()
sll.insert_end(1)
sll.insert_end(2)
sll.insert_end(3)
sll.display()
sll.delete_value(2)
sll.display()









#  Stack unsing sll


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            raise IndexError("Pop from empty stack")
        value = self.top.data
        self.top = self.top.next
        return value

    def peek(self):
        return self.top.data if self.top else None


#
stack = Stack()
stack.push(5)
stack.push(10)
print("Top element:", stack.peek())
print("Popped:", stack.pop())
print("Top after pop:", stack.peek())






