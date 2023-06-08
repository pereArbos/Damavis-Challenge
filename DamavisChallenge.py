# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:16:29 2023

@author: pere
"""



def isCellLegal(labyrinth, cell):
    if (cell[0] < 0 or cell[1] < 0):
        return False
    if (cell[0] >= len(labyrinth) or cell[1] >= len(labyrinth[0])):
        return False
    return labyrinth[cell[0]][cell[1]] == '.'


def isPositionLegal(labyrinth, orientation, head):
    rodCells = [head, [head[0], head[1] -1], [head[0], head[1] -2]]
    if orientation == 'vertical':
        rodCells = [head, [head[0] -1, head[1]], [head[0] -2, head[1]]]
        
    for cell in rodCells:
        if not isCellLegal(labyrinth, cell):
            return False
                   
    return True


def canChangeOrientation(labyrinth, orientation, head):
    center = [head[0], head[1] -1]
    if orientation == 'vertical':
        center = [head[0] -1, head[1]]
        
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if not isCellLegal(labyrinth, [center[0] + x, center[1] + y]):
                return False
            
    return True


def getChangeOrientation(orientation, head):
    if orientation =='horizontal':
        return {'orientation': 'vertical', 'head': [head[0] + 1, head[1] - 1]}
    
    return {'orientation': 'horizontal', 'head': [head[0] - 1, head[1] + 1]}


def getPositionsAfterMoving(labyrinth, orientation, head):
    newHeads = [[head[0] - 1, head[1]],
            [head[0] + 1, head[1]],
            [head[0], head[1] - 1],
            [head[0], head[1] + 1]]
    
    positions = []
    for newHead in newHeads:
        if (isPositionLegal(labyrinth, orientation, newHead)):
            positions.append({'orientation': orientation, 'head': newHead})
    
    if canChangeOrientation(labyrinth, orientation, head):
        positions.append(getChangeOrientation(orientation, head))
        
    return positions


test3 =   [[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".","#",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".","#",".",".",".",".",".",".",".","."],
[".","#",".",".",".","#",".",".",".","."],
[".",".",".",".",".",".","#",".",".","."],
[".",".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".",".","."]]



initialPosition = {'orientation': 'horizontal', 'head': [0, 2]}
labyrinth = test3
goal = [len(labyrinth) - 1, len(labyrinth[0]) - 1]

visitedPositions = {'horizontal': [[0, 2]], 'vertical': []}
currentPaths = [initialPosition]

numberOfMoves = 0
finish = False

while (not finish):
    numberOfMoves += 1
    newPaths = []
    
    for path in currentPaths:
        newPositions = getPositionsAfterMoving(labyrinth, path['orientation'], path['head'])
        for position in newPositions:
            if position['head'] == goal:
                finish = True
            
            if position['head'] in visitedPositions[position['orientation']]:
                continue
            
            newPaths.append(position)
            visitedPositions[position['orientation']].append(position['head'])
            
    currentPaths = newPaths
    if len(currentPaths) == 0:
        numberOfMoves = -1
        finish = True
            
            
print(numberOfMoves)