import cv2
import numpy as np

foto1 = cv2.imread('Foto1.jpg')
foto2 = cv2.imread('Foto2.jpg')

"""rescale = 0.5"""
foto1 = cv2.resize(foto1, (0,0), fx=0.2, fy=0.2)
foto2 = cv2.resize(foto2, (0,0), fx=0.2, fy=0.2)


"""compairing the two images and draw the outline of the things that dont match"""
diff = cv2.absdiff(foto1, foto2)
mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
th, threshed = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY_INV)
"""from foto1 only show the pixels that are not in foto2 (the pixels that are in foto2 are transparent)"""
foto1[threshed==255] = (0,0,0)

# check if the pixels are neighbouring removed pixels in a range of 10 pixels make them black (except around the edges)
for x in range(10, len(foto1)-10):
    for y in range(10, len(foto1[0])-10):
        if foto1[x][y][0] == 0 and foto1[x][y][1] == 0 and foto1[x][y][2] == 0:
            if foto1[x+1][y][0] == 0 and foto1[x+1][y][1] == 0 and foto1[x+1][y][2] == 0:
                foto1[x][y] = (0,0,0)
            elif foto1[x-1][y][0] == 0 and foto1[x-1][y][1] == 0 and foto1[x-1][y][2] == 0:
                foto1[x][y] = (0,0,0)
            elif foto1[x][y+1][0] == 0 and foto1[x][y+1][1] == 0 and foto1[x][y+1][2] == 0:
                foto1[x][y] = (0,0,0)
            elif foto1[x][y-1][0] == 0 and foto1[x][y-1][1] == 0 and foto1[x][y-1][2] == 0:
                foto1[x][y] = (0,0,0)
            elif foto1[x+1][y+1][0] == 0 and foto1[x+1][y+1][1] == 0 and foto1[x+1][y+1][2] == 0:
                foto1[x][y] = (0,0,0)
            elif foto1[x+1][y-1][0] == 0 and foto1[x+1][y-1][1] == 0 and foto1[x+1][y-1][2] == 0:
                foto1[x][y] = (0,0,0)
            elif foto1[x-1][y+1][0] == 0 and foto1[x-1][y+1][1] == 0 and foto1[x-1][y+1][2] == 0:
                foto1[x][y] = (0,0,0)
            elif foto1[x-1][y-1][0] == 0 and foto1[x-1][y-1][1] == 0 and foto1[x-1][y-1][2] == 0:
                foto1[x][y] = (0,0,0)
                


"""show the result"""
cv2.imshow('foto1', foto1)
cv2.imshow('foto2', foto2)
cv2.waitKey(0)
cv2.destroyAllWindows()
