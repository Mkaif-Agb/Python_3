from PIL import Image

img = Image.open("54.jpg")
print(img.format)
print(img.size)
img.show()

img2 = Image.open("371.jpg")
print(img2.size)
print(img2.format)
img2.show()

area = [10 , 10 ,20 , 20]

img.paste(img2 , area)
img.show()