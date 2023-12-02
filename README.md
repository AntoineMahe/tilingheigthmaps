## tilingheightmaps

Python script to create tiles from height maps for use with Unreal Engine 5.

### Usage

```bash
python3 tilling.py -h
```

#### Optional Arguments

- `-i IMAGE_PATH, --image_path IMAGE_PATH`: Path to the original image.
- `-o OUTPUT_PATH, --output_path OUTPUT_PATH`: Path to the folder where the result should be saved.
- `-t TILE_SIZE, --tile_size TILE_SIZE`: Size of the output tiles in pixels.
- `-b, --no_bomb_check`: Boolean to deactivate decompression bomb check, needed for large image files.

### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/tilingheightmaps.git
   cd tilingheightmaps
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python3 tilling.py -i input_image.png -o output_folder -t 256
   ```
### Warning about using '-b' option

This script is meant to be use in a workflow to create tiled landscape in unreal engine, therefore it is expected that the input image may be quite large. 
By default the Pillow library does not allow the decompression of image that would be superior to about 0.25GB. It may be a limitation for our use case, this is why the '--no_bomb_check' has been implemented.
However the decompression of large png image may have the same effect of a DOS attacks. Use with caution.

### Examples

Include some examples of how to use your script with different configurations:

```bash
python3 tilling.py -i input_image.png -o output_folder -t 128
python3 tilling.py -i another_image.png -o output_folder -t 256 -b
```
### Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Create a pull request.

### License

This project is licensed under the GPL-3.0 license - see the [LICENSE](LICENSE) file for details.
