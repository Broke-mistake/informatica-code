from PIL import Image

img1 = Image.open(r'fotos/origineel.jpg')
img2 = Image.open(r'fotos/methoi.jpg')
marge = 50
img3 = Image.new("RGBA", img2.size, (255, 255, 255, 0))

for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))
        pixR1 = int(str(pixel1[0]))
        pixG1 = int(str(pixel1[1]))
        pixB1 = int(str(pixel1[2]))

        if int(str(pixel2[0])) not in range((pixR1-marge), (pixR1+marge)) or int(str(pixel2[1])) not in range((pixG1-marge), (pixG1+marge)) or int(str(pixel2[2])) not in range((pixB1-marge), (pixB1+marge)):
            img3.putpixel((x, y), pixel2)

img3.save("new.png")