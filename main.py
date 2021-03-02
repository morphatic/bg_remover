'''
Following the background image removal tutorial at: https://flothesof.github.io/removing-background-scikit-image.html
'''
# import necessary libraries
from skimage import filters, io as skio
import matplotlib.pyplot as plt

# load our source image
img = skio.imread('./images/tutorial_girl.jpg')

# apply sobel filters to find image outlines
sobel = filters.sobel(img)

# process the image
plt.imshow(sobel)

# save the output to our output directory
plt.savefig('./output/outlines.png')
