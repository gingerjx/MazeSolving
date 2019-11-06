import numpy as np
import cv2 as cv
import math

def find4Points(contour):
        indRight = np.where(contour == np.amax(contour[:,:,0]))
        indLeft = np.where(contour == np.amin(contour[:,:,0]))
        indBottom= np.where(contour == np.amax(contour[:,:,1]))
        indTop = np.where(contour == np.amin(contour[:,:,1]))

        pRight = contour[ indRight[0], indRight[1] ]
        pLeft = contour[ indLeft[0], indLeft[1] ]
        pBottom = contour[ indBottom[0], indBottom[1] ]
        pTop = contour[ indTop[0], indTop[1] ]

        return (pRight,pLeft,pBottom,pTop)

def canBeCircle(diffVer, diffHor, radiusVer, radiusHor,shape):
    if ( shape[0] < shape[1] ):
        size = shape[0]
    else: size = shape[1]
    rad = (radiusVer + radiusHor)/2

    if diffVer <= size/50 and  diffHor <= size/50 and abs(radiusVer - radiusHor) <= size/50 and rad >= size/100 and rad < size/10:
        return True
    else:
        return False

def similar2Circle(cir):    #return % of similarity to circle
    x, y, rad, con = cir
    numOfPoints = len(con)
    allErrors = 0
    for row in con:
        for point in row:
            a = (x-point[0])**2;   b = (y-point[1])**2 
            euklides = math.sqrt( a + b )
            if (rad != 0):
                relativeError = ((abs(rad - euklides)) / rad ) * 100
            else: relativeError = 0
            allErrors += relativeError 
    return (x, y, rad, 100 - allErrors/numOfPoints, con)

def findCircle(propCircle):
    max = 0
    propCirclenSimilarities = []
    for pcir in propCircle:
        x,y,rad,sim, con = similar2Circle(pcir)
        propCirclenSimilarities.append((x,y,rad,sim,con))
        if sim > max:
            max = sim
            start = (x,y,rad,sim, con)                         
    return (start, propCirclenSimilarities)

def findStartnEnd(contours, shape): #find start of the maze
    propCircle = []

    for con in contours:
        con = np.array(con)
        pRight, pLeft, pBottom, pTop = find4Points(con) 

        diffHor = abs(pRight[0][1] - pLeft[0][1])       #diffrence in Y coord between max right point and max left point
        diffVer = abs(pBottom[0][0] - pTop[0][0])       #diffrence in X coord between max top point and max bottom
        radiusHor = (pRight[0][0] - pLeft[0][0])/2      #horizontal radius
        radiusVer = (pBottom[0][1] - pTop[0][1])/2      #vertical radius

        if canBeCircle(diffVer,diffHor,radiusVer,radiusHor, shape):
            radius = (radiusVer + radiusHor)/2
            y = (pRight[0][1] + pLeft[0][1])/2 
            x = (pBottom[0][0] +  pTop[0][0])/2
            propCircle.append([int(x),int(y),int(radius),con])       #propably it is circle
    
    start,propCircle = findCircle(propCircle)                   #looking for shape which is the most similar to circle
    end = findEnd(start,propCircle)                             #looking for shape which is the most similar to start circle

    return (start,end)

def findEnd(start,circles):
    startRad = start[2]
   
    diffRads = []
    for cir in circles:
        if cir[0] == start[0] and cir[1] == start[1]: continue
        diffRads.append(abs(cir[2]-startRad))
    
    diffRads.sort()
    bestRad = diffRads[0]       #the smallest diffrence between possible circles radiuses and start circle radius

    simCircles = []
    for cir in circles:
        if cir[0] == start[0] and cir[1] == start[1]: continue
        if  abs(cir[2]-startRad) == bestRad:
            simCircles.append(cir)
    
    max = 0
    for cir in simCircles:
        similar = cir[3]
        if similar > max:
            max = similar
            end = cir

    return end

def findPoints(contours, shape):
    start, end = findStartnEnd(contours, shape)
    return ( start , end )


