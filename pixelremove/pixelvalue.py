from PIL import Image
img = Image.open(r'')
a = 100
b = 100
pixel = img.load()
im = Image.Image.split(img)
pixR = im[0].load()
pixB= im[1].load()
pixG = im[2].load()
print(img.size)
step = 50
finished = False
while not finished:
    for a in range(a, img.size[0], step):
        print(f"de coordinaten zijn{a, b}")
        print(f"RGB value is {pixR[a, b], pixB[a, b], pixG[a, b]}")
        if a >= img.size[0]-step and b <= img.size[1]:
            # reset de x coordinaar en herhoog de y coordinaat zodat de code rij voor rij de img scanned
            a = 0
            b = b+200
            
        if b >= img.size[1]:
            finished = True
            
        
