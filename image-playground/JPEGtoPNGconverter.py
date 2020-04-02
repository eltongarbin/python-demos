import sys
import os
from pathlib import Path
from PIL import Image

input_path = sys.argv[1]
output_path = sys.argv[2]

Path(output_path).mkdir(exist_ok=True)

for filename in os.listdir(input_path):
    img = Image.open(f'{input_path}/{filename}')
    filename_without_ext = os.path.splitext(filename)[0]
    img.save(f'{output_path}/{filename_without_ext}.png')
    print('all done!')
