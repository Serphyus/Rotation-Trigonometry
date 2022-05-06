import numpy as np
from math import sin, cos, radians

from typing import Union, Tuple, Sequence


Numeric = Union[int, float]

Rotation = Tuple[Numeric, Numeric, Numeric]
Edges = Sequence[Tuple[int, int]]
Vertices = Sequence[np.ndarray]

Shape = Tuple[Vertices, Edges]


def create_matrix(rotation: Rotation) -> np.ndarray:
    """
    creates a general rotation matrix using the rotation provided
    γ : roll  (x rotation)
    β : pitch (y rotation)
    α : yaw   (z rotation)

        [cos(z) cos(y)    cos(z) sin(y) sin(x) - sin(z) cos(x)    cos(z) sin(y) cos(x) + sin(z) sin(x)]
    R = [sin(z) cos(y)    sin(z) sin(y) sin(x) + cos(z) cos(x)    sin(z) sin(y) cos(x) - cos(z) sin(x)]
        [   -sin(y)                    cos(y) sin(x)                          cos(y) cos(x)           ]
    """
    x, y, z = map(radians, rotation)
    
    matrix = np.array([
        [cos(z) * cos(y),    cos(z) * sin(y) * sin(x) - sin(z) * cos(x),    cos(z) * sin(y) * cos(x) + sin(z) * sin(x)],
        [sin(z) * cos(y),    sin(z) * sin(y) * sin(x) + cos(z) * cos(x),    sin(z) * sin(y) * cos(x) - cos(z) * sin(x)],
        [   -sin(y),                      cos(y) * sin(x),                               cos(y) * cos(x)              ]
    ])

    return matrix


def rotate_vertices(vertices: Vertices, matrix: np.ndarray) -> Sequence[Vertices]:
    """performs a calculation of the matrix argument on each vertex"""
    return [np.matmul(matrix, vertex) for vertex in vertices]