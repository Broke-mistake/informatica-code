import cv2
import time
from PIL import Image
time.sleep(2)

vid = cv2.VideoCapture(0)
ret, frame = vid.read()
cv2.imwrite(r'fotos/img1.jpg', frame)
print("1e foto genomen")
time.sleep(5)
vid = cv2.VideoCapture(0)
ret, frame = vid.read()
cv2.imwrite(r'fotos/img2.jpg', frame)
vid.release()
print("2e foto genomen")
img1, img2, marge = Image.open(r'fotos/img1.jpg'), Image.open(r'fotos/img2.jpg'), 20
#variablesen aanzijzen in een efficentere manier 
img3 = Image.new("RGBA", img2.size, (255, 255, 255, 0))

for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        pixel1, pixel2 = img1.getpixel((x, y)), img2.getpixel((x, y))
        if pixel2[0] not in range((pixel1[0]-marge), (pixel1[0]+marge)) or pixel2[1] not in range((pixel1[1]-marge), (pixel1[1]+marge)) or pixel2[2] not in range((pixel1[2]-marge), (pixel1[2]+marge)):
            # ik denk dat dit het snelst is want als 1 er van al waar is dan gaat hij naar het else statment 
            img3.putpixel((x, y), pixel2)
        else:
            pass

img3.save("new.png")
