class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def addChild(self, str):
        if len(str) == 0:
            return

        child = self.findChildNode(str[0])
        if child is None:
            newChild = Node(str[0])
            self.children.append(newChild)

            newChild.addChild(str[1:])
        else:
            child.addChild(str[1:])

    def findChildNode(self, char):
        for child in self.children:
            if child.val == char:
                return child
        return None

    def lookup(self, path="", results=[]):
        if len(self.children) == 0:
            results.append(path+self.val)

        for child in self.children:
            child.lookup(path+self.val, results)

        return results

    def printChildrenVals(self):
        return map(lambda x: x.val, self.children)

class autofill:
    cities = [
        "Atlanta",
        "Boston",
        "Chicago",
        "Dallas",
        "Denver",
        "Detroit",
        "Kansas City",
        "San Diego",
        "San Francisco",
        "San Jose",
        "abc",
        "abd",
        "ghi",
    ]

    root = Node("")

    def lookup(self, str):
        node = self.root
        ind = 0
        while (ind < len(str) and node.findChildNode(str[ind])):
            node = node.findChildNode(str[ind])
            ind += 1

        return node.lookup(str[:ind-1], [])

    def __init__(self):
        for city in self.cities:
            self.addCity(city.lower())

    def addCity(self, city):
        self.root.addChild(city)

    def printTree(self):
        cities = []
        self.printTreeRec(self.root, "", cities)

        print cities

    def printTreeRec(self, root, currPath, cities):
        if root.children == []:
            cities.append(currPath + root.val)

        for child in root.children:
            self.printTreeRec(child, currPath + root.val, cities)

        return

af = autofill()
# af.printTree()
print af.lookup("de")
print af.lookup("denver")
print af.lookup("san")
print af.lookup("")