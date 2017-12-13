class Node:
    val = None
    left = None
    right = None

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def dfs(self, todo, string = ""):
        if len(todo) == 0:
            print string
            return

        node = todo.pop(0)
        string += "" if string == "" else ", "
        string += str(node.val)
        if node.right != None:
            todo = [node.right] + todo
        if node.left != None:
            todo = [node.left] + todo

        self.dfs(todo, string)

    def bfs(self, todo, string = ""):
        if len(todo) == 0:
            print string
            return

        node = todo.pop(0)
        string += "" if string == "" else ", "
        string += str(node.val)
        if node.left != None:
            todo += [node.left]
        if node.right != None:
            todo += [node.right]

        self.bfs(todo, string)

def printTree(root):
    q = [(root,0)]

    tree = {}
    maxLevel = 0
    while len(q) > 0:
        (node, level) = q.pop()
        if node == None:
            continue
        if level not in tree:
            tree[level] = []

        tree[level].append(node.val)

        q.append((node.left, level+1))
        q.append((node.right, level+1))

        if level+1 > maxLevel:
            maxLevel = level+1

    print tree
    for i in range(maxLevel):
        print tree[i][::-1]


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

n1.dfs([n1])
n1.bfs([n1])

printTree(n1)