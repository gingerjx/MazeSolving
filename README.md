# MazeSolving
Project about finding optimal escape path of maze from image.

## Libraries
OpenCV and Numpy

## Maze assumptions

- any shape and color of maze
- start and end are marked by similar circles inside maze
- size of image minimum 500x500 px (otherwise it is expanding)


## How it works:
Conversion image to binary image (walls, start and end - black | empty space - white)

- Finding contours on the image
- Finding start and end point and their features
- Reduction of contours
- Finding escape path ( BFS algorithm )
- Performing result on new image (original image with drawed path)

## Results
<img src="/maze.png" width="200" height="200"><img src="/bfs.gif" width="200" height="200"><img src="/solvedmaze.png" width="200" height="200">
