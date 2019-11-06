from multiprocessing  import Queue
import cv2 as cv
import numpy as np

def finish(point,end,s):
    left = int(s/2)
    corner = [ point[0]-left, point[1]-left ]           #looking for end point starting from leftUpCorner of mask

    for n in range(s):
      for m in range(s):
        if corner[0] + n == end[0] and corner[1] + m == end[1]:
          return True

def drawPath(im,x,y,s):
    left = int(s/2)
    right = s - left

    leftBourder = x-left
    rightBourder = x+right
    upBourder =  y-left
    downBourder = y+right

    im[ leftBourder:rightBourder, upBourder:downBourder ] = 127     

def iswhite(im,x,y,s):
    left = int(s/2)
    right = s - left

    leftBourder = x-left
    rightBourder = x+right
    upBourder =  y-left
    downBourder = y+right

    mat = np.array(im[ leftBourder:rightBourder, upBourder:downBourder ])
    if np.all(mat == 255):
        return True
    else: return False

def getadjacent(n,s):
    x,y = n
    return [(x-s,y),(x,y-s),(x+s,y),(x,y+s)]

def Bfs(image,start, end, radius):
    size = int(radius/2) + (not (int(radius/2)%2))  #finding optimal size of mask
    
    while size > 0:             #look for path as long as size of mask i greater than 0
        queue = Queue()
        queue.put([start])                              #adding start point to queue

        img = image.copy()
        while not queue.empty():

            path = queue.get() 
            pixel = path[-1]

            if finish(pixel,end,size):
                return path,size

            for adjacent in getadjacent(pixel,size):
                x,y = adjacent
                if iswhite(img,x,y,size):
                    drawPath(img,x,y,size)
                    new_path = list(path)
                    new_path.append(adjacent)
                    queue.put(new_path)

        size -= 2          #if path cannot be founded try again with smaller size of mask

    return None,None






