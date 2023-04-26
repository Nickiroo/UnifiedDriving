from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import time
import json
import pandas as pd
import numpy as np
import os
import pygame

def roadMapDisplayInit():
    pygame.init()
    global nodeList
    nodeList = []
    global segmentList
    segmentList = []

    global screen 
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Simulation")
    screen.fill((254,251,234))
    pygame.display.update()

def newCoord(x,y):
    x = x + 600
    y = y + 400
    return x,y

def importRoadInfo():
    with open('road.txt') as f:
        roadSys = f.readlines()
        roadSys = [list(x.strip()) for x in roadSys]
        for i in range(len(roadSys)):
            for j in range(len(roadSys[i])):
                roadSys[i][j] = int(roadSys[i][j])

        for i in range(len(roadSys)):
            if roadSys[i][0] == 1:
                x,y,z = roadSys[i][2], roadSys[i][3], roadSys[i][4]
                roadSys[i][2] = [x,y,z]
                x,y,z = roadSys[i][5], roadSys[i][6], roadSys[i][7]
                roadSys[i][3] = [x,y,z]
                del roadSys[i][4:]
                roadSys[i][2] = int(''.join(map(str, roadSys[i][2])))
                roadSys[i][3] = int(''.join(map(str, roadSys[i][3])))
                


        for i in range(len(roadSys)):
            if roadSys[i][0] == 1:
                nodeList.append(roadSys[i][1:])
            if roadSys[i][0] == 2:
                segmentList.append(roadSys[i][1:])

def printInfo():
    print("These are the nodes: ")
    print(nodeList)
    print("These are the segments: ")
    print(segmentList)

def updateCoords():
    for i in range(len(nodeList)):
        nodeList[i][1], nodeList[i][2] = newCoord(nodeList[i][1], nodeList[i][2])

def plotNodes():
    for i in range(len(nodeList)):
        x = nodeList[i][1]
        y = nodeList[i][2]
        pygame.draw.rect(screen, (0,0,0), (x,y,20,20))
        pygame.display.update()

def plotSegments():
    #loop through segmentList
    for i in range(len(segmentList)):
        #segmentList[i][1] = node1
        #segmentList[i][2] = node2
        #connect node1 to node2
        x1,y1 = nodeList[segmentList[i][1]][1], nodeList[segmentList[i][1]][2]
        x2,y2 = nodeList[segmentList[i][2]][1], nodeList[segmentList[i][2]][2]
        pygame.draw.line(screen, (255,0,0), (x1,y1), (x2,y2), 5);pygame.draw.line(screen, (255,0,0), (x1+17.5,y1+17.5), (x2+17.5,y2+17.5), 5)
        pygame.display.update()

roadMapDisplayInit()

importRoadInfo()
printInfo()
updateCoords()
printInfo()

plotNodes()
plotSegments()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False