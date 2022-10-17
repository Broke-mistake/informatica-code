from PIL import Image, ImageFilter

image = Image.open(r'fotos/joepie.jpg')
image = image.convert("L")
image = image.filter(ImageFilter.FIND_EDGES)
image.save("new3.png")