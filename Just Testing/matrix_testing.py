from PIL import Image
import numpy as np
import sys

# np.set_printoptions(threshold=sys.maxsize)


'''
1. Open an image
2. Take each pixel and change to an rgb value
    make a matrix of rgb values using numpy
3. Observe original matrix values
4. Scale image using scaling algorithm
5. Observe new matrix values

6. Find the coefficients of the matrix?
'''

im = Image.open('black_star.jpg')
width, height = im.size

# convert image into an array of rgb values
imrgb = im.convert('RGB')

# gets the data as a list using getdata() from PIL
pixel_values = list(imrgb.getdata())# gets rgb values
print(pixel_values)
print('list length: ', len(pixel_values))

# find a way to create a numpy array of tuples that contain rgb values

# creates a numpy array from the list generated by getdata()
# reshape just makes it so that the array dimensions match the image dimensions
m = np.asarray(pixel_values).reshape((width, height))
# keep track of data in console
print('og img matrix:\n', m, '\n')
print('num of pixels in og img: ', m.size)
print('og img dimensions: ', m.shape, '\n')


