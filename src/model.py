import numpy as np

from core import Vertices, Edges, Shape


class Model:
    def __init__(self,
            vertices: Vertices,
            edges: Edges = None,
        ) -> None:
        
        self._vertices = vertices
        self._edges = edges


    def rotate(self, matrix: np.ndarray) -> None:
        """multiplies the rotation matrix with each of the models vertices"""
        self._vertices = [np.matmul(matrix, vertex) for vertex in self._vertices]


    def get_vertices(self) -> Vertices:
        return self._vertices


    def get_shape(self) -> Shape:
        return [self._vertices, self._edges]