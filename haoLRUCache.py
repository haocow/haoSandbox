class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v

        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}

        self.head = Node(-1,0)
        self.tail = Node(-1,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.size = 0

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)

            return node.val

        return -1

    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
            self.size -= 1

        new = Node(key, val)
        self.add(new)
        self.cache[key] = new
        self.size += 1

        if self.size > self.capacity:
            delKey = self.tail.prev.key
            self.remove(self.tail.prev)
            self.size -= 1
            del self.cache[delKey]

    def add(self, node):
        node.prev = self.head
        node.next = self.head.next

        headNext = self.head.next
        self.head.next = node
        headNext.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def printLL(self):
        string = ""
        curr = self.head.next
        while curr != None:
            string = string + " " + str(curr.val)
            curr = curr.next

        print string[1:-2]




lru = LRUCache(2)
lru.put(1,1)
lru.put(3,3)

lru.printLL()

lru.get(1)

lru.printLL()
