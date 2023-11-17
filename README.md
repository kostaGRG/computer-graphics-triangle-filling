# Computer Graphics: Triangle Filling
## Intro
This project is created for the university class named Computer Graphics at Aristotle University of Thessaloniki (AUTh). It's the first out of three repositories referenced on the same class.

## General
### Files
In this repository code is written on the following files:
* triangle_filling.py: This file contains Python source code, and in it, the functions interpolate_color, shade_triangle, and render are implemented as requested in the assignment.
* demo_flat.py: A Python file that utilizes the functions found in the previous file, using flat shading.
* demo_gouraud.py: A Python file that utilizes the functions found in the previous file, using Gouraud shading.
* hw1.npy: Data file.

More specifically, the demo files initially load the data from the hw1.npy file and then call the render function, with the shade_t argument taking the value flat/gouraud accordingly. The assignment is implemented in Python, and the numpy library is used for handling arrays, while matplotlib is used for displaying and saving the generated image.

### Coloring Types
1. Flat: The color for each pixel within the triangle is determined by the average of the colors of its three vertices.
2. Gouraud: Gouraud shading is more complex compared to flat shading, and its implementation involves the interpolate_color function, which selects the appropriate color using linear interpolation. Specifically, the color for each pixel of the triangle is calculated in two stages. First, linear interpolation is performed for the two active points based on their distance from the vertices of the side they are on. In the second stage, another linear interpolation is performed, this time between the desired point and the two active points.

## Functions
### Function: Interpolate color
Create a function that implements linear interpolation between two three-dimensional values C1 and C2 based on the two-dimensional coordinates of two points x1 and x2 of the vertices of a triangle.
value = interpolate_color(x1, x2, x, C1, C2)
where:
* x1 and x2 are the corresponding components of the two-dimensional coordinates of two vertices of a triangle (either horizontal or vertical coordinates).
* C1 and C2 are the three-dimensional color values corresponding to the coordinates x1 and x2.
* x is the point at which interpolation will be applied.
* value is the result of linear interpolation between C1 and C2.

### Function: Shade Triangle
The purpose of this assignment is to implement a triangle filling algorithm based on the polygon filling algorithm described in the notes. After adapting the algorithm from the notes to handle the special case of triangles, consider the two different color rendering approaches described below.
Let there be a triangle defined by vertices with integer coordinates. Assume a canvas of dimensions M × N. Create the function:

Y = shade_triangle(img, verts2d, vcolors, shade_t)

Where:

* img is the image (an array of dimensions M × N × 3) with any pre-existing triangles.
* verts2d is an integer array of dimensions 3 × 2, with each row containing the two-dimensional coordinates of a vertex of the triangle.
* vcolors is an array of dimensions 3 × 3, with each row containing the color of a vertex of the triangle in RGB format (with values in the range [0, 1]).
* shade_t is a string argument that can take values ["flat", "gouraud"], where in each case, the corresponding variation of the triangle filling algorithm will be performed, and it differs in how the color is calculated.
* Y is an array of dimensions M × N × 3, which, for all points within the triangle, contains the calculated color components (Ri, Gi, Bi) as well as any pre-existing triangles from the input img (covering any common colored points that existed from the filling of other triangles).

![Triangle Colouring](/images/colouring.png)


1. Implementation with the argument shade_t = "flat":
In the shade_triangle function with the argument shade_t = "flat", each triangle will be assigned a unique color. Specifically, each triangle will be colored with the color that results from the centroid (average) of the colors of its vertices.

2. Implementation with the argument shade_t = "gouraud":
In the shade_triangle function with the argument shade_t = "gouraud", it will calculate the color of the points within the triangle using linear interpolation from the colors of its vertices. Specifically, for the coloring of the triangle, with reference to the points in Figure 1, the colors at positions A and B will first be calculated using the interpolate_color function for the color values of vertices V1, V3, and V1, V2 respectively (providing the appropriate coordinates of the vertices of the triangle). This first phase is performed once for each scanline y.

In the second phase, linear interpolation must be performed again for each point P = (x, y) belonging to the current scanline, using the interpolate_color function.

### Function: Object colouring
Implement the function:
img = render(verts2d, faces, vcolors, depth, shade_t)
Where:
* img is a color image of dimensions M × N × 3. The image will contain K colored triangles
that form the projection of a 3D object in 2 dimensions.
* verts2d is the array with the vertices of the triangles in the image. The verts2d array is
of size L × 2 and contains the coordinates of a multitude of L vertices. For simplification,
assume that all vertices are within the canvas.
* faces is the array that contains the vertices of the K triangles. The array is of size K × 3.
The i-th row of the array declares the three vertices that form the triangle (with reference
to vertices of the verts2d array and numbering starting from 1).
* vcolors is the array with the colors of the vertices. The vcolors array is of size L × 3.
The i-th row of the array declares the color components of the corresponding vertex.
* depth is the array that declares the depth of each vertex before the projection of the object
in 2 dimensions. The depth array is of size L × 1.
* shade_t is a similar control variable (of string type) that determines the shading function
(Gouraud or Flat) to be used, and can take values ["flat", "gouraud"].
* M and N are the height and width of the canvas, respectively.
Inside the render function, the shade_triangle function will be called, which, depending on
the value of the shade_t variable, will call the corresponding routine for coloring the interior
points of each triangle. The order in which triangles should be colored is determined by the depth
array. Coloring should start from the farthest (those with the highest depth) triangles and continue
with the closest ones. The depth of a triangle is calculated as the center of gravity of the depths of its vertices.
Consider that:
1. The background of the canvas is white (rgb = (1,1,1)).
2. The canvas has dimensions M = 512, N = 512.

## Assumptions
* The algorithm stores points with inverted coordinates only so that they are properly projected by the function we use.
* In the image projection, the larger y values are located at the bottom of the axis, so the code of the shade_triangle function is sufficient for the correct handling of horizontal lines.
* In general, an attempt was made to follow the pseudocode of the third chapter of the posted notes on the class, however, some simplifications were made to the algorithm due to the use of exclusively triangles and not general polygons. One such example is the non-counting of even/odd intersections.
* Additionally, since active points may have decimal values, rounding to the nearest pixel is performed (in the code: int(x+0.5)).

## Results
1. Flat colouring
   
![Image with flat colouring](/images/result_flat.png)

2. Gouraud colouring

![Image with Gouraud colouring](/images/result_gouraud.png)
