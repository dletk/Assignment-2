from PIL import Image
import glob, os

im1 = Image.open("original.jpg")
im2 = Image.open("original copy.jpg")

im3 = Image.blend(im1, im2, 0.5)
im3.show()