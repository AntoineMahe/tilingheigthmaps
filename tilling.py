#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import datetime
from PIL import Image
import logging
import os


class ImageDivider:
    """class to handle image tile division."""

    def __init__(self, input_image_path, output_folder, tile_size, no_bomb_check):
        self.logger = logging.getLogger(__name__)
        self.image_path = input_image_path
        self.output_folder = output_folder
        self.tile_size = tile_size
        if no_bomb_check:
            Image.MAX_IMAGE_PIXELS = None  # disabling DecompressionBomb check
            self.logger.warning("PIL decompression bomb check deactivate.")
        self.logger.info(f"ImageDivider initialized with input_image_path={input_image_path}, output_folder={output_folder}, tile_size={tile_size}, no_bomb_check={no_bomb_check}.")

    def divide_image(self):
        # Open the image
        original_image = Image.open(self.image_path)   # .convert("L")  # Convert to grayscale should not be needed
        original_image_name = "".join(self.image_path.split('/')[-1].split('.')[:-1])
        # Ensure the output folder exists
        os.makedirs(self.output_folder, exist_ok=True)

        # Get image dimensions
        width, height = original_image.size

        # Calculate the number of squares in each dimension
        num_squares_x = width // self.tile_size
        num_squares_y = height // self.tile_size

        self.logger.info(f"Original image is about to get tiled into {num_squares_x}x{num_squares_y} square.")
        # Iterate through the squares
        for y in range(num_squares_y):
            for x in range(num_squares_x):
                # Crop the square
                left = x * self.tile_size
                upper = y * self.tile_size
                right = left + self.tile_size
                lower = upper + self.tile_size

                square = original_image.crop((left, upper, right, lower))

                # Save the square as a new image
                output_path = os.path.join(
                    self.output_folder, f"{original_image_name}_{x}_{y}.png"
                )
                square.save(output_path)
                self.logger.debug(f"Saved {original_image_name}_{x}_{y}.png.")

if __name__ == "__main__":

    logging.basicConfig(format='%(name)s %(asctime)s %(levelname)s %(message)s',  level=logging.INFO)
    # arg parser for input settings
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image_path', type=str, help='path to the original img')
    parser.add_argument('-o', '--output_path', type=str, help='path to the folder where the result should be saved')
    parser.add_argument('-t', '--tile_size', type=int, help='size of the ouptut tiles in pixel')
    parser.add_argument('-b', '--no_bomb_check', action='store_true', help='boolean to deactivate decompression bomb check, needed for large image file', default=False)

    args = parser.parse_args()

    # Input image path
    input_image_path = args.image_path

    # Output folder for squares
    output_folder = args.output_path

    # Size of each subsquare
    tile_size = args.tile_size

    # Decompression bomb check:
    no_bomb_check = args.no_bomb_check

    # Run the function
    divider = ImageDivider(input_image_path, output_folder, tile_size, no_bomb_check)
    divider.divide_image()
