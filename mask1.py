import numpy as np
import cv2
import time

mask_color = (0.0,0.0,0.0) #tuple 
subtraction = cv2.createBackgroundSubtractorMOG2() # maak een substractor object
frame = cv2.imread(cv2.samples.findFile(r'fotos/img7.jpg'))
mask = subtraction.apply(frame)
mask_stack = np.dstack([mask]*3)
mask_stack = mask_stack.astype('float32') / 255.0
frame = frame.astype('float32') / 255.0
masked = (mask_stack * frame) + ((mask_stack))
masked = (masked * 255).astype('uint8') 
cv2.imwrite(f'fotos/default.jpg', frame)

# while True:
#     cv2.imshow("default", frame)

#     # cv2.imshow("OpenCV Method", mask)