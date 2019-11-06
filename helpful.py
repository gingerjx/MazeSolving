import cv2 as cv
import numpy as np

def contoursReduction(contours):
    contoursReduced = []   #Reduction of contours
    if ( len(contours) ) > 300:
        for i in contours:
            if len(i) > 100:
                contoursReduced.append(i)
    else:
        contoursReduced = contours
    return contoursReduced;

def drawWithoutPoints(img,cons,start,end):
    for x in cons:
        if np.all(x == start[4]) or np.all(x == end[4]) : continue
        else:  img = cv.drawContours(img,[x],0,0,1)

    startRad = start[2]
    endRad = end[2]
    cv.circle(img,start[:2],startRad,255,-1)
    cv.circle(img,end[:2],endRad,255,-1)
    return img

def drawPath(img,path,start,end,s):
    for position in path:
       drawPoint(img,position,s)
    cv.circle(img,((start[0],start[1])),start[2],(0,0,255),-1)
    cv.circle(img,((end[0],end[1])),end[2],(0,0,255),-1)

def drawPoint(img,point,s):
    left = int(s/2)
    right = s - left
    x,y = point
    img[x-left:x+right,y-left:y+right] = (255,0,0)