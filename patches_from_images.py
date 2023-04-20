import PIL
import argparse
from PIL import Image
from image_manager import split_images_in_patches



def main():
    PIL.Image.MAX_IMAGE_PIXELS = 933120000
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", default='', help="path to the original images.")
    parser.add_argument("--output_path", default='', help="path where the output patches will be stored.")
    args = parser.parse_args()

    split_images_in_patches(args.input_path, args.output_path, stop_at=900)

if __name__ == "__main__":
    main()
