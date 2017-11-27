class Test:
    val = None

    def __init__(self, init1):
        self.val = init1

    def getVal(self):
        return self.val

testObj = Test("Jon Hao")
print testObj.getVal()