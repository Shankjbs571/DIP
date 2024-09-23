
import cv2
# from google.colab.patches import cv2_imshow   #to be used with google colab cv2.imshow() is not supported
import numpy as np
import ast
import matplotlib.pyplot as plt

'''
This part takes in a 3 channel image, reads it and saves as a 3D matrix, like: [[[r1,g1,b1],...,[r_w,g_w,b_w]],...,[[r_h,g_h,b_h],...,[r_w,g_w,b_w]]] 
'''
r = 0 
c = 0 
image = cv2.imread('/content/448892009_463743449740641_6190272654554746437_n.jpg')
with open("image_matrix_with_brackets.txt", "w") as file:
        file.write("[\n")  
        for row in image:
            r+=1
            c = 0
            file.write("  [")  
            for pixel in row:
                c+=1
                file.write(f"[{pixel[0]}, {pixel[1]}, {pixel[2]}], ")  
            file.write("],\n")  
            print("columns: ",c)
        file.write("]\n")  
        print("rows: ",r)
        


'''
Here we can take any .txt file having the 3D matrix, 

It will read that and convert to python list and then numpy array for further usecase
'''
with open("/content/image_matrix_with_brackets.txt", "r") as file:
    data = file.read()

image_matrix = ast.literal_eval(data)

image_matrix = np.array(image_matrix)

grid_height, grid_width, _ = image_matrix.shape
square_size = 1 
print("grid_height:",grid_height)
print("grid_width:",grid_width)




'''
for the image used as example, it has 600 x 450 as dimension

this python code contructs the matplotlib plot with 600 x 450 squares and fills each square with rbg pixel value from 3D matrix as facevalue
'''
grid_width = 450
grid_height = 600
square_size = 10  

fig, ax = plt.subplots(figsize=(grid_width / 100, grid_height / 100))

ax.set_xlim(0, grid_width)
ax.set_ylim(0, grid_height)
ax.set_aspect('equal')

ax.axis('off')

for x in range(0,grid_width): 
    for y in range(0,grid_height): 
        rgb_color = image_matrix[y,x][::-1] / 255.0
        square = plt.Rectangle((x, y), square_size, square_size, facecolor=rgb_color, edgecolor='none')
        ax.add_patch(square)
    # if x==100:
    #   break

plt.show()

