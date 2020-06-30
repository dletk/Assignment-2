# Install the package Pillow:   pip install pillow
from PIL import Image

# The documentation is here,
# https://pillow.readthedocs.io/en/stable/reference/Image.html#
# please just look at the Image Module and Image Class section
# Read about this module/class and its relevant information, but dont worry about other classes/modules for now
# (unless you have to)


# Read an image using Pillow, using filename
old_image = Image.open(input())

# Open the old image

# In the terminal, hit enter to continue
input("HIT ENTER TO CONTINUE......")

new_image = Image.open(input())

# Loop over an image, pixel by pixel
for x in range(old_image.width):
    for y in range(old_image.height):
        pixel_value = old_image.getpixel((x, y))
        new_pixel = new_image.getpixel((x, y))
        if pixel_value >= (240, 240, 240):
            old_image.putpixel((x, y), (new_pixel[0], new_pixel[1], new_pixel[3]))
    




# ===================== ASSIGNMENT ===========================

# Please create a Python module (.py file) contains AT LEAST 3 FUNCTIONS as follow:
# 1. Apply a filter (like instagram filter) of your choice to a given image (input: filename)
# 2. Rotate an image 90 degree (do not use the rotate function of PIL), using pixel modification (cpying and moving pixel around) (like above) (input: fileName).
# 3. HARD: Given an image with white background, replace the background with a given background image (input: originalFileName, backgroundFileName)

