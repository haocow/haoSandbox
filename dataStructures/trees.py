class Node:
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if (self.val < val):
            if (self.left == None):
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if (self.right == None):
                self.right = Node(val)
            else:
                self.right.insert(val)


class Tree:
    root = None

    def __init__(self, val):
        self.root = Node(val)

    def insert(self, val):
        self.root.insert(val)

    def printTree(self):
        tree = {}
        queue = [(self.root, 0)]

        while (len(queue) > 0):
            (currNode, currLevel) = queue.pop()

            if (len(tree) <= currLevel):
                tree[currLevel] = []

            addVal = None if currNode == None else currNode.val
            tree[currLevel].append(addVal)

            if currNode.left != None:
                queue.append((currNode.left, currLevel+1))
            if currNode.right != None:
                queue.append((currNode.right, currLevel+1))

        print tree

tree = Tree(5)
tree.insert(3)
tree.insert(9)
tree.insert(4)
tree.insert(10)
tree.insert(7)
tree.insert(100)
tree.insert(88)
tree.printTree()
