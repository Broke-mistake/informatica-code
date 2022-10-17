import numpy as np
import cv2
import datetime
# premask = Image.open(r'fotos/new2.jpg')
# vid = cv2.VideoCapture(0)
# vid.release()

subtraction = cv2.createBackgroundSubtractorMOG2()
mask_color = (0.0,0.0,0.0)


kernel = np.ones((5,5),np.uint8)
# counter = 0
# while counter <= 2:
# ret, frame = vid.read()

# Apply background subtraction to create a mask
frame = cv2.imread(cv2.samples.findFile(r'fotos/img1.jpg'))

#img3=img1 - img2
mask = subtraction.apply(frame)


# mask = cv2.dilate(mask, None, iterations=10)
# mask = cv2.erode(mask, None, iterations=10) 
# mask = cv2.GaussianBlur(mask, (21, 21), 0)

# Create 3-channel alpha mask
mask_stack = np.dstack([mask]*3)
# Ensures data types match up
mask_stack = mask_stack.astype('float32') / 255.0
frame = frame.astype('float32') / 255.0
# nodig voor het neuralnetwork om het te begrijpen want anders kan het niet rekene met de matrixen
masked = (mask_stack * frame) + ((1-mask_stack) * mask_color)
masked = (masked * 255).astype('uint8') 


frame = cv2.imread(cv2.samples.findFile(r'fotos/img2.jpg'))

mask = subtraction.apply(frame)


# mask = cv2.dilate(mask, None, iterations=10)
# mask = cv2.erode(mask, None, iterations=10)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.GaussianBlur(mask, (21,21), 0)
# Create 3-channel alpha mask
mask_stack = np.dstack([mask]*3)
# Ensures data types match up
mask_stack = mask_stack.astype('float32') / 255.0
frame = frame.astype('float32') / 255.0
# Blend the image and the mask
masked1 = (mask_stack * frame) + ((1-mask_stack) * mask_color)

masked2=masked1-masked
masked3 = (masked1 * 255).astype('uint8')

cv2.imshow("OpenCV Method", masked3)
cv2.imwrite(f'fotos/bla.jpg', masked3)
# cv2.imwrite(f'fotos/{datetime.datetime.now().hour}-{datetime.datetime.now().minute}-{datetime.datetime.now().second}.jpg', masked1)

