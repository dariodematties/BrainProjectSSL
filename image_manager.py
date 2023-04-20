import os
import numpy as np
from PIL import Image
from patchify import patchify
from fastai.imports import Path




def split_image_in_patches(image_path, output_path, left=400, top=400, right=20400, bottom=20400):
    image = Image.open(image_path)
    image=image.crop((left, top, right, bottom))
    image = np.asarray(image)
    patches = patchify(image, (512, 512), step=512)

    for i in range(patches.shape[0]):
        for j in range(patches.shape[1]):
            patch = patches[i, j]
            patch = Image.fromarray(patch)
            num = i * patches.shape[1] + j
            patch.save(os.path.join(output_path, os.path.splitext(os.path.basename(image_path))[0] + f"_patch_{num}.jpg"))



def split_images_in_patches(images_dir, output_path, stop_at=1):
    for k, filename in enumerate(os.listdir(images_dir)):
        folder_name = os.path.splitext(filename)[0]
        Path(os.path.join(output_path, folder_name)).mkdir(parents=True, exist_ok=True)
        f = os.path.join(images_dir, filename)

        # checking if it is a file
        if os.path.isfile(f):
            print(f)
            print(k)
            split_image_in_patches(f, os.path.join(output_path, folder_name))
            if k >= stop_at:
                break




