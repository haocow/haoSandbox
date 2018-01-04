class Heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def push(self, val):
        self.heap.append(val)
        self.size += 1

        self.percUp(self.size)

    def pop(self):
        if self.size == 0:
            return None
        else:
            retVal = self.heap[1]
            self.heap[1] = self.heap[self.size]
            self.heap = self.heap[:-1]
            self.size -= 1
            self.percDown(1)

            return retVal

    def percUp(self, ind):
        while ind != 0:
            if self.heap[ind/2] > self.heap[ind]:
                tmp = self.heap[ind]
                self.heap[ind] = self.heap[ind/2]
                self.heap[ind/2] = tmp
            ind = ind/2

    def percDown(self, ind):
        while ind*2 <= self.size:
            minChild = ind*2 if ((ind*2) + 1) > self.size or self.heap[ind*2] < self.heap[(ind*2) + 1] else (ind*2) + 1
            if self.heap[minChild] < self.heap[ind]:
                tmp = self.heap[minChild]
                self.heap[minChild] = self.heap[ind]
                self.heap[ind] = tmp
            ind = minChild

heap = Heap()
heap.push(4)
heap.push(3)
heap.push(5)
heap.push(7)
heap.push(2)
print heap.heap
print heap.pop()
print heap.heap
