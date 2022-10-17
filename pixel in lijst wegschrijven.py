from PIL import Image

# https://pillow.readthedocs.io/en/stable/reference/index.html
# 
img1 = Image.open(r'fotos/origineel.jpg')
img2 = Image.open(r'fotos/methoi.jpg')
img1 = img1.convert("RGBA")
img2 = img2.convert("RGBA")

# im = Image.Image.split(img2)

img3 = Image.new("RGBA", img2.size, (255, 255, 255, 0))
# img3.show()

for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        pixel1 = img1.getpixel((x, y))
        pixel2 = img2.getpixel((x, y))
        
        if pixel1 != pixel2:
            # marge toe voegen voor beter resultaat 
            img3.putpixel((x, y), pixel2)

img3.save("new.png")
