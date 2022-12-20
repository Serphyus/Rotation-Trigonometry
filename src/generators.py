import numpy as np
from itertools import product
from math import radians, cos, sin

from core import Shape


class Generators:
    __all__ = [
        'cube',
        'sphere'
    ]


    @staticmethod
    def cube(radius: float, iterations: int) -> Shape:
        vertices = []
        edges = []

        fraction = (radius * 2) / (iterations)
        
        points = []
        for i in range(iterations + 1):
            points.append((i * fraction) - radius)

        vertices = [*map(np.array, product(points, repeat=3))]

        return vertices, edges
        

    @staticmethod
    def sphere(radius: float, rings: int) -> Shape:
        vertices = []
        edges = []

        for vertical in range(rings):
            v_angle = radians((360 / rings) * vertical)
            for horizontal in range(rings):
                h_angle = radians((360 / rings) * horizontal)

                x = radius * cos(v_angle) * cos(h_angle)
                y = radius * cos(v_angle) * sin(h_angle)
                z = radius * sin(v_angle)

                vertices.append(np.array((x, y, z)))

        return vertices, edges