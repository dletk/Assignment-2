# Install the package Pillow:   pip install pillow
from PIL import Image

# The documentation is here,
# https://pillow.readthedocs.io/en/stable/reference/Image.html#
# please just look at the Image Module and Image Class section
# Read about this module/class and its relevant information, but dont worry about other classes/modules for now
# (unless you have to)


# Read an image using Pillow, using filename
old_image = Image.open("./images/sample.jpg")

# Open the old image
old_image.show()

# In the terminal, hit enter to continue
input("HIT ENTER TO CONTINUE......")

new_image = Image.new("RGB", old_image.size)

# Loop over an image, pixel by pixel
for x in range(old_image.width):
    for y in range(old_image.height):
        # Get the value of the current pixel in the old image, it will be a tuple in format (R,G,B)
        pixel_value = old_image.getpixel((x, y))
        
        # Update the value of the new image with the value from the old image pixel, but using Red=255
        new_image.putpixel((x,y), (255, pixel_value[1], pixel_value[2]))

# Show the newly modified image, tada
new_image.show()

# ===================== ASSIGNMENT ===========================

# Please create a Python module (.py file) contains AT LEAST 3 FUNCTIONS as follow:
# 1. Apply a filter (like instagram filter) of your choice to a given image (input: filename)
# 2. Rotate an image 90 degree (do not use the rotate function of PIL), using pixel modification (cpying and moving pixel around) (like above) (input: fileName).
# 3. HARD: Given an image with white background, replace the background with a given background image (input: originalFileName, backgroundFileName)

