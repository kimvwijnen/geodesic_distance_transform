import numpy as np
import imageio
import pydicom
import matplotlib.pyplot as plt
from compute_distance_map import compute_dm_rasterscan

def normalize_im(I):
    normed_im = 255. * (1. * I - np.amin(I))/(np.amax(I)-np.amin(I))
    return normed_im

seeds = np.array([[363,186]])
dist_type = 'geodesic'
iterations = 2
filename = 'example/input.dcm' #'example/input.png'
save_im = False

im = imageio.imread(filename)

im = normalize_im(im) * 255.

dm = compute_dm_rasterscan(im, seeds, its=iterations, dist_type=dist_type)
plt.imshow(dm)
plt.show()

if save_im:
    imageio.imwrite('example/' + dist_type + '_distance_map.png', dm)
