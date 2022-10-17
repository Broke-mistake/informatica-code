from PIL import Image
img1 = Image.open(r'fotos\targetachtergrond.png')
img2 = Image.open(r'fotos\target.png')
img2 = img2.convert("RGBA")
img1 = img1.convert("RGBA")
datas2 = img2.getdata()
datas1 = img1.getdata()
for item2 in datas2:

    for item1 in datas1:
        if item2[0] == item1[0] and item2[1] == item1[1] and item2[2] == item1[2]:
            item2 = (255, 255, 255, 0)
            
        # else:
        #     list_of_pixels.append(item2)


# Do something to the pixels...
# img2 = Image.new(im.mode, im.size)
# img2.putdata(list_of_pixels)

img2.putdata(item2)
img2.save("target1", "PNG")     
