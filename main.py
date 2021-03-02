'''
Following the background image removal tutorial at: https://flothesof.github.io/removing-background-scikit-image.html
'''
from skimage import io as skio

img = skio.imread('./images/tutorial_girl.jpg')
print("shape of image: {}".format(img.shape))
print("dtype of image: {}".format(img.dtype))
