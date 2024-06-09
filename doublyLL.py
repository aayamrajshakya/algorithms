class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                if current == self.head:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                    if current == self.tail:
                        self.tail = current.prev
                return True
            current = current.next
        return False

    def tailDisplay(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()

    def tailRemove(self, value):
        current = self.tail
        while current is not None:
            if current.data == value:
                if current == self.tail:
                    self.tail = current.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    if current.next is not None:
                        current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return True
            current = current.prev
        return False

# Main function
if __name__ == "__main__":
    LL = LinkedList()
    LL.append(5)
    LL.append(33)
    LL.append(1)
    LL.append(7)
    LL.append(33)
    LL.append(12)
    LL.display()
    LL.remove(33)
    LL.display()
    LL.prepend(12)
    LL.display()
    LL.remove(13)
    LL.display()
    LL.tailDisplay()
    LL.tailRemove(12)
    LL.display()
