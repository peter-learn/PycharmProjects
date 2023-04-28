import random, time, copy, os
WIDTH = 40
HEIGHT = 20


nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    nextCells.append(column)
while True:
    print('\n\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end=" ")
        print()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            numNeighoors = 0
            #print(len(currentCells[19]))#1234543243234
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighoors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighoors += 1
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighoors += 1
            if currentCells[leftCoord][y] == '#':
                numNeighoors += 1
            if currentCells[rightCoord][y] == '#':
                numNeighoors += 1
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighoors += 1
            if currentCells[x][belowCoord] == '#':
                numNeighoors += 1
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighoors += 1
            if currentCells[x][y] == '#' and (numNeighoors == 2 or numNeighoors == 3):
                nextCells[x][y] = '#'
            elif  currentCells[x][y] == '' and numNeighoors == 3:
                nextCells[x][y] = '#'
            else:
                nextCells[x][y] = ' '
    time.sleep(1)
