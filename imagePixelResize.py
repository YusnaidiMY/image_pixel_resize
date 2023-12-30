'''
A routine to resize image to any desired size. For example, a user 
can resize original images taken from smartphone in high resolution
such as 1024x1024 pixels to as small as 1x1 dimensions. Similarly,
the routine can perform image resizes from poor resolution
to high resolution (however, with to poor resolution since
the program is not meant to perform image reconstruction).
The routine can perform image resizing all at once for all images in
the input folder.

For best performance, stick to perform image resizing from 
high resolution images to a small resolution images, for example,
from 1024x1024 pixel image to 320x320 pixel image.

The only changes you need to do to run this routine is to change
the image input location (input_folder) to match the location
of the images to resize.


Author: Yusnaidi Md Yusof
Email: yusnaidi.kl@utm.my
Date: 30.12.2023
Copyright RFTI@UTM.

--------------------------------

IMPORTANT: Change the input_folder to the path to your image input folder.
Example: Change: input_folder = r"PATH_TO_YOUR_INPUT_FOLDER" (line 73) to
                 input_folder = r"C:\Users\username\Documents\input_image"
'''
from PIL import Image
import os

def resize_image(input_path, output_path, size=(4, 4)):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            img_resized = img.resize(size)
            
            # Extract the filename and extension
            filename, extension = os.path.splitext(os.path.basename(input_path))

            # Append the size to the filename
            new_filename = f"{filename}-to-{size[0]}x{size[1]}{extension}"

            # Save the resized image with the new filename
            output_path = os.path.join(output_path, new_filename)
            img_resized.save(output_path)
            print(f"Image resized to {size} pixels and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def convert_images_to_size(input_folder, output_folder, size=(4, 4)):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Process each file in the input folder
    for file in files:
        # Check if the file is a JPG or PNG image
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Create the input and output file paths
            input_path = os.path.join(input_folder, file)

            # Resize the image and save with the specified size in the filename
            resize_image(input_path, output_folder, size)

# Specify the input and output folders
input_folder = r"PATH_TO_YOUR_INPUT_FOLDER"
output_folder = os.path.join(input_folder, "output_images_resized")

# Get user input for the desired size
user_input = input("Enter the desired size for resizing (e.g., '32x32'): ")
width, height = map(int, user_input.split('x'))
size = (width, height)

# Call the function to convert images to the specified size and save with the new filename
convert_images_to_size(input_folder, output_folder, size)
