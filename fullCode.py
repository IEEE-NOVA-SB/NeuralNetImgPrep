import os
import rembg
from PIL import Image

# Set the input and output directories
input_dir = '/home/drifter/projects/remove-background/editar'
output_dir = '/home/drifter/projects/remove-background/completo'

# Iterate over all files in the input directory
for file_name in os.listdir(input_dir):
    if file_name.endswith('.jpg') or file_name.endswith('.png') or file_name.endswith('.jpeg'):
        # Open the image and remove the background using Rembg
        with open(os.path.join(input_dir, file_name), 'rb') as f:
            image = Image.open(f)

            output = rembg.remove(image)
            output = output.convert('RGB')#Porque não consegue converter imagens .jpeg. pois imagens .jpeg têm um canal alpha

        # Save the output image to the output directory
        output_file = os.path.join(output_dir, file_name)
        with open(output_file, 'wb') as f:
            output.save(f)
