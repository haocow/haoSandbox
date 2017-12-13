map1 = [
    [0,0,1,1,0],
    [0,0,0,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [1,1,0,0,1],
]

map2 = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
]

map3 = [
    [1,0,1,0,1],
    [0,0,1,0,0],
    [1,0,1,0,1],
    [0,0,1,0,0],
    [1,0,1,0,1],
]

def numIslands(mapIn):
    visited = []
    numIsl = 0
    for i in range(len(mapIn)):
        visited.append([0] * len(mapIn))

    for i in range(len(mapIn)):
        for j in range(len(mapIn)):
            if mapIn[i][j] == 0 and visited[i][j] == 0:
                visited[i][j] = 1
            elif visited[i][j] == 0:
                floodIsland(i, j, visited, mapIn)
                numIsl += 1

    return numIsl

def floodIsland(i, j, visited, mapIn):
    queue = [(i,j)]

    while (len(queue) > 0):
        (i,j) = queue.pop(0)
        visited[i][j] = 1

        if i > 0 and mapIn[i-1][j] == 1 and visited[i-1][j] == 0:
            queue.append((i-1, j))
        if i < len(mapIn)-1 and mapIn[i+1][j] == 1 and visited[i+1][j] == 0:
            queue.append((i+1, j))
        if j > 0 and mapIn[i][j-1] == 1 and visited[i][j-1] == 0:
            queue.append((i, j-1))
        if j < len(mapIn)-1 and mapIn[i][j+1] == 1 and visited[i][j+1] == 0:
            queue.append((i, j+1))

assert(numIslands(map1) == 3)
assert(numIslands(map2) == 1)
assert(numIslands(map3) == 7)