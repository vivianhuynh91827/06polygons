import math
from display import *

#vector functions
#normalize vetor, should modify the parameter
def normalize(vector):
    pass

#Return the dot porduct of a . b
def dot_product(a, b):
    return (a[0]*b[0] + a[1]*b[1] + a[2]*b[2])

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    p0 = i
    p1 = i + 1
    p2 = i + 1

    a = [polygons[p1][0]-polygons[p0][0],
        polygons[p1][1]-polygons[p0][1],
        polygons[p1][2]-polygons[p0][2]]

    b = [polygons[p2][0]-polygons[p0][0],
        polygons[p2][1]-polygons[p0][1],
        polygons[p2][2]-polygons[p0][2]]

    x = a[1]*b[2]-a[2]*b[1]
    y = a[2]*b[0]-a[0]*b[2]
    z = a[0]*b[1]-a[1]*b[0]
    return [x,y,z]
