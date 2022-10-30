import cv2

foto2 = cv2.imread('Foto1.jpg')
foto1 = cv2.imread('Foto2.jpg')

# zorgen dat je de gehele foto kan zien
if foto1.shape[0] >=1000 and foto1.shape[1] >=1000:
    foto1 = cv2.resize(foto1, (0,0), fx=0.2, fy=0.2)
if foto2.shape[0] >=1000 and foto2.shape[1] >=1000:
    foto2 = cv2.resize(foto2, (0,0), fx=0.2, fy=0.2)

#het verschil tussen de foto's berekenen wat we eerst deden door pixel voor pixel te vergelijken is nu dit:
diff = cv2.absdiff(foto1, foto2)
# de foto grijs maken en de threshold aanmaken, zonder dit werkt het niet
mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
th, threshed = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY_INV)

"""convert the image to RGBA"""
foto1 = cv2.cvtColor(foto1, cv2.COLOR_BGR2BGRA)

"""make the pixels that are not in foto2 transparent"""
foto1[threshed==255] = (0,0,0,0)

# """approximate-nearest-neighbor-search"""
# foto1 = cv2.resize(foto1, (0,0), fx=1, fy=1, interpolation=cv2.INTER_NEAREST)

"""for non transparent pixels, check if they are in the proximity of 10 transparent pixel in a range of 80 pixels"""
for i in range(0, foto1.shape[0]):
    for j in range(0, foto1.shape[1]):
        if foto1[i,j,3] != 0:
            if (foto1[max(0,i-5):min(foto1.shape[0],i+5),max(0,j-5):min(foto1.shape[1],j+5),3] == 0).sum() > 55:
                foto1[i,j,3] = 0

cv2.imwrite('result1.png', foto1)