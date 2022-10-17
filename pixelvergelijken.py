from PIL import Image
img = Image.open(r'img.png')
img1 = Image.open(r'img1.png')
img = img.convert("RGBA")
img1 = img1.convert("RGBA")
finished = False
a = 100
b = 100
pixel = img.load()
pixel1 = img1.load()
if img.size != img1.size:
    print(error)
    finished = True
step = 50
while not finished:
    for a in range(a, img.size[0], step):
        for b in range(b, img.size[1], step):
            for c in range(0, img1.size[0], step):
               for d in range(0, img1.size[1], step):
                if pixel[a,b] == pixel1[c,d]:
                    pixel1[c,d] = (0,0,0,0)
                    img1.save(r'code/img1')
                if b+100 >= img1.size[1]:
                    finished = True
            
        