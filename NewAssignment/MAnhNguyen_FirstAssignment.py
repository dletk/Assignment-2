# First Python Assginment with package Pillow
# Name: Mai Anh Nguyen
# Due date: June 15th, 2020

# Install the package Pillow: pip install pillow
# Import the modules Image and ImageFilter from Pillow package
from PIL import Image, ImageFilter

# Task 1: Apply a filter (like instagram filter) of your choice to a given image (input: filename)
# Filter image1 with EMBOSS filter
def image_filter(image):
    image.filter(filter = ImageFilter.EMBOSS).show()
    # Show the newly filtered image

# Read an image using Pillow, using filename
image1 = Image.open(input("Enter the filename: "))

# Open the image1
image1.show()

# In the terminal, hit enter to continue
input("HIT ENTER TO CONTINUE......")

# Filter image1
image_filter(image1)

input("HIT ENTER TO CONTINUE......")
# End of Task 1

# Task 2: Rotate image 90 degree (do not use the rotate function of PIL), using pixel modification.
def rotate_image(img):
    # Create variable "pixel" and load the pixel data of img into that variable
    pixel = img.load()

    # Create a new image with the given mode and size
    rotate_img = Image.new("RGB", (img.height, img.width))

    # Create variable "pixel_new" and load the pixel data of rotate_image into that variable
    pixel_new = rotate_img.load()

    # Loop over an image, pixel by pixel
    for y in range(img.height):
        for x in range(img.width):
            # Rotate image1 by reversing the coordinates of each pixel in img
            pixel_new[y, image1.width - x - 1] = pixel[x, y]

    # Show the newly rotated image
    rotate_img.show()

# Rotate image1
rotate_image(image1)
# End of task 2

# Task 3: Given an image with white background, replace the background with a given background image (input: originalFileName, backgroundFileName)
def change_background(img1, img2):
    pixel1 = img1.load()

    pixel2 = img2.load()

    # Loop over an image, pixel by pixel
    for x in range(img1.width):
        for y in range(img1.height):
            # Replace the values of any pixels with white color in img1 image by corresponding pixel values in img2 image
            if pixel1[x, y] >= (240, 240, 240):
                pixel1[x, y] = pixel2[x, y]

    # Show the newly modified img1 image.
    img1.show()

white_background = Image.open(input("Enter the filename of image with white background: "))

white_background.show()

different_background = Image.open(input("Enter the filename of image with different background: "))

# Resize the different_background image if its size is different from white_background's size. 
background2 = different_background.resize((white_background.size))

background2.show()

# Replace background of white_background image
change_background(white_background, background2)
# End of task 3
