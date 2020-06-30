from PIL import Image

original_fileName = Image.open(input())
 
background_fileName = Image.open(input())

background2 = background_fileName.resize((original_fileName.size))

pixel = original_fileName.load()

pixels = background2.load()

width, height = original_fileName.size

for x in range(width):
    for y in range(height):
        if pixel[x, y] >= (240, 240, 240):
            pixel[x, y] = pixels[x, y]

original_fileName.show()