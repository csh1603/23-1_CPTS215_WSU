from HeapPrac import *
from GraphPr import *

def prims_algorithm(aGraph, start):
    pq = BinaryHeap()
    start.set_distance(0)
    pq.build_heap([(v, v.get_distance()) for v in aGraph])
    while not pq.is_empty():
        curr_tuple = pq.del_min()
        currV = curr_tuple[0]
        for adjV in currV.get_connections():
            new_cost = currV.get_weight(adjV)
            adjV_tuple = (adjV, adjV.get_distance())
            if adjV_tuple in pq and new_cost < adjV.get_distance():
                adjV.set_distance(new_cost)
                adjV.set_predecessor(currV)
                pq.decrease_key((adjV, new_cost))

class DisjoingSet:
    def __init__(self, elements = None):
        self.parent = {}
        self.rank = {}
        for e in elements:
            self.parent[e] = e
            self.rank[e] = 0

    def find(self, element):
        try:
            if self.parent[element] == element:
                return element
            else:
                return self.find(self.parent[element])
        except KeyError:
            return None

    def union(self, first, second):
        first_parent = self.find(first)
        second_parent = self.find(second)

        if first_parent == second_parent:
            pass
        else:
            if self.rank[first_parent] > self.rank[second_parent]:
                self.parent[second_parent] = first_parent
                self.rank[first_parent] += 1
            elif self.rank[first_parent] < self.rank[second_parent]:
                self.parent[first_parent] = second_parent
                self.rank[second_parent] += 1
            else:
                self.parent[second_parent] = first_parent
                self.rank[first_parent] += 1

    def kruskals_algorithm(self):
        MST = Graph()
        pq = BinaryHeap()
        S = DisjoingSet(self.vert_list.keys())

        for V in self.vert_list.values():
            for AV in V.get_connections():
                edge = ((V, AV), V.get_weight(AV))
                pq.insert(edge)
        while not pq.is_empty():
            curr_tuple = pq.del_min()
            currE = curr_tuple[0]
            if S.find(currE[0].get_ID()) == S.find(currE[1].get_ID()):
                pass
            else:
                S.union(currE[0].get_ID(), currE[1].get_ID())
                MST.add_edge(currE[0].get_ID(), currE[1].get_ID())

        return MST

    