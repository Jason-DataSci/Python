%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import skimage.color as color

a = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
b = [[[0.1,0.2,0.3]]]
color.rgb2lab(b)


color.lab2rgb(color.rgb2lab(b))
