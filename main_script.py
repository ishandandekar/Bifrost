# Contains the main graph which acts as a database
from typing import Dict, List, Tuple


class Graph:
    def __init__(self) -> None:
        self.vertices: list = []
        self.vert_neigh_dict: Dict[str, List[Tuple[str, int]]] = {}

    def add_relation(self, start: str, end: str, time: int):
        if start not in self.vertices:
            self.vertices.append(start)
        if end not in self.vertices:
            self.vertices.append(end)
        if self.vert_neigh_dict[start] == None:
            self.vert_neigh_dict[start] = []
        if self.vert_neigh_dict[end] == None:
            self.vert_neigh_dict[end] = []
        self.vert_neigh_dict[start].append((end, time))
        self.vert_neigh_dict[end].append((start, time))

    @property
    def vertices_(self):
        return self.vertices

    def get_neighbours(self, vertex: str):
        if vertex in self.vertices:
            return [neighbour for neighbour, time in self.vert_neigh_dict[vertex]]
        else:
            raise KeyError(f'{vertex} not present as a vertex in database')
