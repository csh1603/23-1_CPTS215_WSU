from collections import deque
from HeapPrac import *

class Vertex:
    def __init__(self, key):
        self.ID = key
        self.connected_to = {}

    def get_ID(self):
        return self.ID

    def get_connections(self):
        return self.connected_to.keys()

    def add_neighbor(self, neighbor, weight = 0):
        self.connected_to[neighbor] = weight

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        self.num_vertices += 1
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    def add_edge(self, start_key, end_key, cost = 0):
        if start_key not in self.vert_list:
            self.add_vertex(start_key)
        if end_key not in self.vert_list:
            self.add_vertex(end_key)
        self.vert_list[start_key].add_neighbor(self.vert_list[end_key], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __contains__(self, item):
        return item in self.vert_list

    def __iter__(self):
        return iter(self.vert_list.values())

def bfs(g, start):
    frontier_queue = deque()
    frontier_queue.appendleft(start)
    discovered_set = set([start])

    while len(frontier_queue) > 0:
        curr_v = frontier_queue.pop()
        print(curr_v)
        for adj_v in curr_v.get_connections():
            if adj_v not in discovered_set:
                frontier_queue.appendleft(adj_v)
                discovered_set.add(adj_v)

def dfs(g, start):
    frontier_stack = deque()
    frontier_stack.append(start)
    discovered_set = set()

    while len(frontier_stack) > 0:
        curr_v = frontier_stack.pop()
        if curr_v not in discovered_set:
            print(curr_v)
            discovered_set.add(curr_v)
            for adj_v in curr_v.get_connections():
                frontier_stack.append(adj_v)

def dijkstras_algorithm(aGraph, start):
    pq = BinaryHeap()
    start.set_distance(0)
    pq.build_heap([(v, v.get_distance()) for v in aGraph])
    while not pq.is_empty():
        curr_tuple = pq.del_min()
        currV = curr_tuple[0]
        for adjV in currV.get_connections():
            new_dist = currV.get_distance() + currV.get_weight(adjV)
            if new_dist < adjV.get_distance():
                adjV.set_distance(new_dist)
                adjV.set_predecessor(currV)
                pq.decrease_key((adjV, new_dist))