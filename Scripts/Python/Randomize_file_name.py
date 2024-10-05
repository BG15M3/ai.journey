import os
import random

# Define the folder containing your images
image_folder = 'C:\photo_rename'

# List all files in the folder
image_files = os.listdir(image_folder)

# Filter the list to only include image files (optional)
image_files = [f for f in image_files if f.endswith(('jpg', 'jpeg', 'png', 'gif'))]

# Shuffle the file names
random.shuffle(image_files)

# Rename each image file with a random number prefix to randomize them
for i, filename in enumerate(image_files):
    new_filename = f"{i+1}_{filename}"
    old_filepath = os.path.join(image_folder, filename)
    new_filepath = os.path.join(image_folder, new_filename)
    os.rename(old_filepath, new_filepath)

print(f"Randomized and renamed {len(image_files)} image files!")
