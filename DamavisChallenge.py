# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:16:29 2023

@author: pere
"""

from functions import getPositionsAfterMoving

from tests import tests


testNumber = input('Enter acceptance test number from 1 to 4 (you can edit them in tests.py):')

labyrinth = tests[int(testNumber) -1]

initialPosition = {'orientation': 'horizontal', 'head': [0, 2]}
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