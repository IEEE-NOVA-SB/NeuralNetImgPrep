# Importing the libraries that will be used in the code.
import os
import rembg
from PIL import Image

# Defining the input and output directories.
input_dir = '/home/drifter/projects/remove-background/editar'
output_dir = '/home/drifter/projects/remove-background/completo'

# Iterating over all the files in the input directory, and if the file is a jpg, png or jpeg, it opens
# the file, removes the background, and saves the file in the output directory.
for file_name in os.listdir(input_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):
        
        # Opening the file, removing the background, and saving the file in the output directory.
        with open(os.path.join(input_dir, file_name), 'rb') as f:
            image = Image.open(f)

            output = rembg.remove(image)
            output = output.convert('RGB')#Porque não consegue converter imagens .jpeg. pois imagens .jpeg têm um canal alpha

        # Joining the output directory and the file name.
        output_file = os.path.join(output_dir, file_name)

        # Saving the file in the output directory.
        with open(output_file, 'wb') as f:
            output.save(f)
