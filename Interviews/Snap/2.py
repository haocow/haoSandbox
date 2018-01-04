class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def get(self, key):
        if key == self.key:
            return self.val
        elif key > self.key and self.right is not None:
            return self.right.get(key)
        elif key < self.key and self.left is not None:
            return self.left.get(key)
        else:
            return None

    def put(self, key, val):
        if key == self.key:
            self.val = val
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, val)
            else:
                self.right.put(key, val)
        else:
            if self.left is None:
                self.left = Node(key, val)
            else:
                self.left.put(key, val)

    def printMe(self):
        if self.left is not None:
            self.left.printMe()
        print self.key, self.val
        if self.right is not None:
            self.right.printMe()

class sortedMap:
    iterStack = []

    def __init__(self):
        self.root = None
        self.size = 0

    def __iter__(self):
        curr = self.root
        while curr is not None:
            self.iterStack.append(curr)
            curr = curr.left
        return self

    def next(self):
        if len(self.iterStack) == 0:
            raise StopIteration()

        retVal = self.iterStack[-1]
        node = self.iterStack[-1]
        self.iterStack.pop()
        if node.right is not None:
            curr = node.right
            while curr is not None:
                self.iterStack.append(curr)
                curr = curr.left

        return retVal

    def get(self, key):
        return self.root.get(key)

    def put(self, key, val):
        if self.root is not None:
            self.root.put(key, val)
        else:
            self.root = Node(key, val)

        self.size += 1

        return

    def size(self):
        return self.size

    def printTree(self):
        if self.root == None:
            return None
        else:
            self.root.printMe()

sm = sortedMap()
sm.put("f", "EFF")
sm.put("b", "BEE")
sm.put("g", "JEE")
sm.put("c", "SEE")
sm.put("e", "YI")
sm.put("d", "DEE")
sm.put("h", "AYCH")
sm.put("a", "AAAYyyyyy")

# print sm.printTree()

# assert(sm.get("a") == "hello")
# assert(sm.get("b") == "BEE")
# assert(sm.get("") == None)
# assert(sm.get("sadfasdfasdfa") == None)

for i in sm:
    print i.key, i.val

# 1,2,3,4,5,6,7,8,9
# 1->2->3->4...