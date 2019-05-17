import numpy as np
import imageio
import pydicom
import matplotlib.pyplot as plt
from compute_distance_map import compute_dm_rasterscan

def normalize_im(I):
    normed_im = (1. * I - np.amin(I))/(np.amax(I)-np.amin(I))
    return normed_im

filename = 'example/input.png'
dist_type = 'geodesic'
iterations = 2
save_im = True

# load intensity image
im = imageio.imread(filename)

# define foreground
seeds = np.array([[363,186]])

# scaling the input image influences the weight between
# euclidean and intensity distance in the final distance map
im = normalize_im(im) * 255.

# compute distance map
dm = compute_dm_rasterscan(im, seeds, its=iterations, dist_type=dist_type)

if save_im:
    save_filename = 'example/' + dist_type + '_distance_map.png'
    plt.imsave(save_filename, dm, cmap='viridis')
    print('Saved as ' + save_filename)
else:
    plt.imshow(dm)
    plt.show()
