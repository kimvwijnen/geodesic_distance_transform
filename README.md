# (Geodesic) Distance Transform

Python implementation of Geodesic Distance Transform (GDT) using Raster Scan for 2D and 3D images. 

Based on the paper "New geodesic distance transforms for gray-scale images" by Toivanen et al (1996) and taigw's C++ version (github.com/taigw/geodesic_distance).

This code computes a distance map given an input image and one or multiple seed points. The type of distance used in the distance map can be Euclidean distance, intensity distance or geodesic distance which combines both. The weighting between intensity distance and Euclidean distance can be varied when computing the geodesic distance map.

![example_gdm_code](https://user-images.githubusercontent.com/29973428/57921170-06281700-789d-11e9-99fb-c636e8821e52.png)

# Run example
- Change the parameters in 'example_code.py' to the desired settings
- Run 'python example_code.py'
- Check the result in the example directory
