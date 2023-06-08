# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 21:16:29 2023

@author: pere
"""

from functions import getPositionsAfterMoving

from tests import tests


testNumber = input('Enter acceptance test number from 1 to 4 (you can edit them in tests.py):')

labyrinth = tests[int(testNumber) -1]

# rod position is stored as the orientation and which cell the head is in
initialPosition = {'orientation': 'horizontal', 'head': [0, 2]}
goal = [len(labyrinth) - 1, len(labyrinth[0]) - 1]

# history of rod positions to avoid moving in circles
visitedPositions = {'horizontal': [[0, 2]], 'vertical': []}
# all paths for the rod that could potentially get to the goal
currentPaths = [initialPosition]

numberOfMoves = 0
finish = False

# loop finishes if goal is reached or ther is no path left that can reach it
while (not finish):
    numberOfMoves += 1
    newPaths = []
    
    for path in currentPaths:
        # calculate all new possible positiotns for every path
        newPositions = getPositionsAfterMoving(labyrinth, path['orientation'], path['head'])
        for position in newPositions:
            if position['head'] == goal:
                finish = True
            
            # avoid moving in circles
            if position['head'] in visitedPositions[position['orientation']]:
                continue
            
            newPaths.append(position)
            visitedPositions[position['orientation']].append(position['head'])
            
    currentPaths = newPaths
    if len(currentPaths) == 0:
        numberOfMoves = -1
        finish = True
            
            
print(numberOfMoves)