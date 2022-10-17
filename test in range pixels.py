from PIL import Image

img1, img2, marge = Image.open(r'fotos/origineel.jpg'), Image.open(r'fotos/methoi.jpg'), 40
img3 = Image.new("RGBA", img2.size, (255, 255, 255, 0))

for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        pixel1, pixel2 = img1.getpixel((x, y)), img2.getpixel((x, y))
        if pixel2[0] not in range((pixel1[0]-marge), (pixel1[0]+marge)) or pixel2[1] not in range((pixel1[1]-marge), (pixel1[1]+marge)) or pixel2[2] not in range((pixel1[2]-marge), (pixel1[2]+marge)):
            img3.putpixel((x, y), pixel2)

img3.save("new.png")
