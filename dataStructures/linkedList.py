class Node:
    val = None
    next = None

    def __init__(self, val):
        self.val = val
        self.next = None

    def setNext(self, newNode):
        self.next = newNode

class LinkedList:
    head = None
    tail = None

    def __init__(self, val):
        self.head = Node(val)
        self.tail = self.head

    def insert(self, newVal):
        newNode = Node(newVal)
        self.tail.setNext(newNode)
        self.tail = newNode

    def remove(self, val):
        curr = self.head

        if (curr.val == val):
            self.head = curr.next
            return

        while (curr):
            if (curr.next != None and curr.next.val == val):
                curr.next = curr.next.next
            curr = curr.next

    def reverse(self):
        self.tail = self.head
        curr = self.head

        revNext = None
        while (curr):
            temp = curr.next
            curr.next = revNext
            revNext = curr
            curr = temp

        self.head = revNext

    def printList(self):
        curr = self.head
        result = []
        while (curr):
            result.append(curr.val)
            curr = curr.next

        print result

ll = LinkedList(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.printList()

ll.reverse()
ll.printList()

ll.remove(4)
ll.printList()
