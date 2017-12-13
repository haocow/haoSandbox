def heapify(nums):
    heap = [0]
    heapSize = 0

    for num in nums:
        heapSize += 1
        heapInsert(heap, num, heapSize)

    return heap

def heapInsert(heap, val, size):
    heap.append(val)
    percUp(heap, size)

    return

def heapPeek(heap):
    return heap[1]

def heapPop(heap):
    min = heap[1]
    heapSize = len(heap) - 1

    heap[1] = heap[heapSize]
    del(heap[-1])

    percDown(heap, 1, heapSize-1)

    return min

def percUp(heap, ind):
    while heap[ind // 2] != 0:
        if heap[ind] < heap[ind // 2]:
            tmp = heap[ind // 2]
            heap[ind // 2] = heap[ind]
            heap[ind] = tmp

        ind = ind // 2

    return

def percDown(heap, ind, heapSize):
    while ind * 2 <= heapSize:
        minChild = ind * 2 if (((ind * 2) + 1) > heapSize or heap[ind * 2] < heap[(ind * 2) + 1]) else ((ind * 2) + 1)

        if heap[minChild] < heap[ind]:
            tmp = heap[ind]
            heap[ind] = heap[minChild]
            heap[minChild] = tmp

        ind = minChild

    return

heap = heapify([7,6,5,4,3,2,1])
assert(heap == [0,1,4,2,7,5,6,3])
assert(heapPop(heap) == 1)
assert(heap == [0,2,4,3,7,5,6])
