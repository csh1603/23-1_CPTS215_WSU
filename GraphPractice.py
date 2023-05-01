class Graph:
    def __init__(self):
        self.ver_list = {}
        self.adj_matrix = [[None]]
        self.num_vertices = 0

    def add_vertex(self, key):
        temp_list = self.adj_matrix
        for i in range(len(self.ver_list)):
            if self.ver_list[i] == key:
                return i

        self.ver_list[self.num_vertices] = key
        self.num_vertices += 1
        self.adj_matrix = [[None for i in range(self.num_vertices)]for j in range(self.num_vertices)]
        for s in range(len(temp_list)):
            for t in range(len(temp_list[s])):
                if temp_list[s][t] is not None:
                    self.adj_matrix[s][t] = 1

        return self.num_vertices - 1

    def add_edge(self, v1, v2):
        i = self.add_vertex(v1)
        j = self.add_vertex(v2)

        self.adj_matrix[i][j] = 1
        self.adj_matrix[j][i] = 1

    def __str__(self):
        represent_list = ""
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] is not None:
                    represent_list += "(" + str(self.ver_list[i]) + ", " + str(self.ver_list[j]) + ")\n"
        return represent_list

def main():
    G = Graph()
    G.add_vertex(2)
    G.add_vertex(1)
    G.add_vertex(3)
    G.add_vertex(6)
    G.add_vertex(5)
    G.add_vertex(4)

    G.add_edge(1, 2)
    G.add_edge(1, 5)
    G.add_edge(2, 3)
    G.add_edge(2, 5)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    G.add_edge(4, 6)
    G.add_edge(7, 5)

    print(G)

if __name__ == "__main__":
    main()