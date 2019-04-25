(Geodesic) Distance Transform

Python implementation of Geodesic Distance Transform (GDT) using Raster Scan for 2D and 3D images. 

Based on the paper "New geodesic distance transforms for gray-scale images" by Toivanen et al (1996) and taigw's C++ version (github.com/taigw/geodesic_distance).

An image and the coordinates of seed points are required to compute the distance map.

The weighting between intensity distance and Euclidean distance can be varied when computing the geodesic distance map. The code also allows for computing a distance map based on Euclidean distance or intensity distance, instead of geodesic distance. 
