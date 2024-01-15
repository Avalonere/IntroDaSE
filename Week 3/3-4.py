class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def len(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.next
            count += 1
        return count

    def items(self):
        current = self.head
        while current is not None:
            yield current.item
            current = current.next

    def find(self, item):
        return item in self.items()

    def add(self, item):
        head = Node(item)
        head.next = self.head
        self.head = head

    def append(self, item):
        tail = Node(item)
        if self.is_empty():
            self.head = tail
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = tail

    def insert(self, item, index):
        if index <= 0:
            self.add(item)
        if index > (self.len() - 1):
            self.append(item)
        else:
            node = Node(item)
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node

    def index(self, item):
        if not self.find(item):
            return -1
        count = 0
        current = self.head
        while current.item != item:
            current = current.next
            count += 1
        return count

    def remove(self, item):
        if not self.find(item):
            return -1
        loc = self.index(item)
        if loc == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(loc - 1):
            current = current.next
        current.next = current.next.next
