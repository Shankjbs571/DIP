# Digital Image Processing

## Overview
This repository contains Python scripts focused on digital image processing.  
Each script aims to explore different aspects of image manipulation, analysis, and visualization. The goal is to implement intuitive and practical code for working with images, making it easier to understand and apply various digital image processing techniques.

### Future Additions
More scripts will be added to cover a wide range of topics, including but not limited to:
- Bitplane Slicing
- Histogram Processing




# Script Descriptions

<table>
    <tr>
        <td><strong>SCRIPT 01 : </strong> image_matrix_reconstructor.py <a href='https://colab.research.google.com/drive/1RF9uR73bFuCAIsSWO4bba_fM9BDCrJo0?usp=sharing' >Open in Google Colab</a> </td>
    </tr>
    <tr>
        <td>

This script takes an image and turns it into a grid of small squares that represent each pixel. Each square is filled with the color of the pixel it represents.

# How It Works
1. **Load Image**: The script loads an image.
2. **Extract Pixels**: It gets the RGB values for each pixel.
3. **Create 3D Matrix**: The pixel values are saved in a 3D matrix and written to a text file.
4. **Plot with Matplotlib**: The script uses Matplotlib to create a plot where each square is filled with the corresponding pixel color.

# What You See
The result is a colorful plot made of squares. It looks like the original image but is actually just a collection of squares representing the pixels.
</td>
    </tr>
    <tr>
        <td>
            <table>
                <tr>
                    <td style="text-align: center;">
                        <h4>Original Image</h4>
                        <img src="/result_images/original_image.png" alt="Image 1" style="width: 300px;">
                    </td>
                    <td style="text-align: center;">
                        <h4>Matrix to BGR</h4>
                        <img src="/result_images/matrix_to_bgr.png" alt="Image 2" style="width: 300px;">
                    </td>
                    <td style="text-align: center;">
                        <h4>Matrix Plot RGB</h4>
                        <img src="/result_images/matrix_plot_rgb.png" alt="Image 3" style="width: 300px;">
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>

