import cv2 as cv
import numpy as np
import points
import helpful
import solve
import time

t0 = time.time()
img = cv.imread("mazes/maze3.jpg")
if  img is None:
    print("Wrong path to file")
    exit(1)
imX, imY = img.shape[0], img.shape[1]
if ( imX * imY < 500*500 ):
    out = cv.resize(img,(500,500))      #resizing image less than 500x500
else: out = img.copy()

grayscale = cv.cvtColor(out,cv.COLOR_BGR2GRAY)
threshold = cv.adaptiveThreshold(grayscale,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11, 2)
contours, hierarchy = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)    #finding contours

start, end = points.findPoints(contours, out.shape)             #returns coordinates and radius of start and end point
if start is None:
    print("Cannot find start and end points.")
else:
    contours = helpful.contoursReduction(contours)                  #Reduce useless contours

    conImg = np.ones((out.shape[0], out.shape[1]), dtype=np.uint8)*255              #creating white image
    conImg = helpful.drawWithoutPoints(conImg,contours,start,end)                   #drawing contours on image


    print("Solving....")
    path, size = solve.Bfs(conImg,(start[1],start[0]),(end[1],end[0]),start[2])     #finding path

    if path is not None:
        helpful.drawPath(out, path, start, end, size)                                   #drawing path in out image
        cv.imwrite("/home/piotrek/PycharmProjects/MazeSolving/mazes/solvedMaze.jpg", out)
    else:
        print ("Cannot find escape path.")

    print("Finish after: ", time.time()-t0, "seconds")
