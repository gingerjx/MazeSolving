Project about finding optimal escape path of maze from image.  
Strucuture of maze:  
-any shape and color of maze  
-start and end are marked by similar circles inside maze  
-size of image minimum 500x500 px (otherwise it is expanding)  
  
Using libraries: OpenCv and Numpy - image processing  
Using BFS algorithm to finding optimal escape path  
  
Program being tested by few images and photos of maze  
  
How it works:  
-Conversion image to binary image (walls, start and end - black | empty space - white)  
-Finding contours on the image  
-Finding start and end point and their features  
-Reduction of contours  
-Finding escape path  
-Performing result on new image (original image with drawed path)  
