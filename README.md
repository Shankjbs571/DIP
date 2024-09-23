# Image Matrix Reconstructor

## What It Is
This project takes an image and turns it into a grid of small squares that represent each pixel. Each square is filled with the color of the pixel it represents.

## How It Works
1. **Load Image**: The script loads an image.
2. **Extract Pixels**: It gets the RGB values for each pixel.
3. **Create 3D Matrix**: The pixel values are saved in a 3D matrix and written to a text file.
4. **Plot with Matplotlib**: The script uses Matplotlib to create a plot where each square is filled with the corresponding pixel color.

## What You See
The result is a colorful plot made of squares. It looks like the original image but is actually just a collection of squares representing the pixels.

## How to Use It
1. Make sure you have Python and these packages:
   ```bash
   pip install matplotlib numpy
