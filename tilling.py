#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = None  # disabling DecompressionBomb check

def divide_image(image_path, output_folder, tile_size):
    # Open the image
    original_image = Image.open(image_path)   # .convert("L")  # Convert to grayscale should not be needed
    original_image_name = "".join(image_path.split('/')[-1].split('.')[:-1])
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get image dimensions
    width, height = original_image.size

    # Calculate the number of squares in each dimension
    num_squares_x = width // tile_size
    num_squares_y = height // tile_size

    # Iterate through the squares
    for y in range(num_squares_y):
        for x in range(num_squares_x):
            # Crop the square
            left = x * tile_size
            upper = y * tile_size
            right = left + tile_size
            lower = upper + tile_size

            square = original_image.crop((left, upper, right, lower))

            # Save the square as a new image
            output_path = os.path.join(
                output_folder, f"original_image_name_{x}_{y}.png"
            )
            square.save(output_path)

if __name__ == "__main__":

    # arg parser for input settings
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image_path', type=str, help='path to the original img')
    parser.add_argument('-o', '--output_path', type=str, help='path to the folder where the result should be saved')
    parser.add_argument('-t', '--tile_size', type=int, help='size of the ouptut tiles in pixel')

    args = parser.parse_args()

    # Input image path
    input_image_path = args.image_path

    # Output folder for squares
    output_folder = args.output_path

    # Size of each subsquare
    tile_size = args.tile_size

    # Run the function
    divide_image(input_image_path, output_folder, tile_size)
