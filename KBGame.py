##############################################
# Title: PA6 - KB Game
# Author: Seunghyun Cho
# Version: 3.10.6
# Date: Apr 23rd, 2023
#
# Description: This program implements BFS.
##############################################

# Vertex class
class Vertex:
    # initialization method
    def __init__(self, key):
        self.ID = key
        self.connected_to = {}
        self.distance = 0

    # method for getting Vertex's ID
    def get_ID(self):
        return self.ID

    # method for getting connected Vertexes
    def get_connections(self):
        return self.connected_to.keys()

    # method for adding neighbor and adds distance (how many it is connected to)
    def add_neighbor(self, neighbor, weight = 0):
        self.connected_to[neighbor] = weight

    # method for getting weight
    def get_weight(self, neighbor):
        return self.connected_to[neighbor]

    # method for getting distances between Vertexes
    def get_distance(self):
        return self.distance

class Graph:
    # method for initialization
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    # method for connecting vertexes
    def add_vertex(self, key):
        if key not in self.vert_list:
            self.num_vertices += 1
            new_vertex = Vertex(key)
            self.vert_list[key] = new_vertex
            return new_vertex

    # method for getting vertex in particular index
    def get_vertex(self, n):
        if n in self.vert_list:
            return self.vert_list[n]
        else:
            return None

    # method for making connection
    def add_edge(self, start_key, end_key, cost = 0):
        if start_key not in self.vert_list:
            self.add_vertex(start_key)
        if end_key not in self.vert_list:
            self.add_vertex(end_key)
        if self.vert_list[end_key] in self.vert_list[start_key].get_connections():
            return
        self.vert_list[start_key].add_neighbor(self.vert_list[end_key], cost)

    # method that returns every vertex in graph
    def get_vertices(self):
        return self.vert_list.keys()

    # method for getting distance
    def get_distance(self, n):
        return self.vert_list[n].get_distance()

    # method for finding particular element is contained
    def __contains__(self, n):
        return n in self.vert_list

    # method for iterating
    def __iter__(self):
        return iter(self.vert_list.values())


# Breadth-First-Search, subgraph
def BFS(g, start, goal):

    start = g.get_vertex(start)
    goal = g.get_vertex(goal)

    # list for tracking nodes what we had explored so far
    explored = []
    # queue for keeping nodes what we have to explore
    queue = [[start]]

    # If the start node is already the goal node return None
    if start == goal:
        return

    # repeat until the queue is empty
    while queue:
        path = queue.pop(0)
        vertex = path[-1]

        # if current node is already explored, continue
        if vertex not in explored:
            neighbors = vertex.get_connections()
            # check every connected nodes
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                # check whether neighbour node is the goal or not
                if neighbor == goal:
                    goal.distance = len(new_path) - 1
                    return new_path

            explored.append(vertex)
    # if no path is find, return None
    return



def main():
    # opening actors ID and name file
    actors_file = open(r"actors.txt", "r", encoding="latin-1")
    actors_list = {}

    while True:
        line = actors_file.readline()
        if not line: break
        line = line.strip()
        line = line.split('|')
        actors_list[int(line[0])] = line[1]
    actors_file.close()

    # open the file with movie ID & actors ID
    movie_actors_file = open(r"movie-actors.txt", "r", encoding="latin-1")
    movie_actors_list = {}

    while True:
        line = movie_actors_file.readline()
        if not line: break
        line = line.strip()
        line = line.split('|')
        for i in range(1):
            if int(line[0]) in movie_actors_list:
                movie_actors_list[int(line[0])].append(int(line[1]))
            else:
                movie_actors_list[int(line[0])] = [int(line[1])]
    movie_actors_file.close()

    # open the file with movie ID and name
    movie_file = open(r"movies.txt", "r", encoding="latin-1")
    movie_list = {}

    while True:
        line = movie_file.readline()
        if not line: break
        line = line.strip()
        line = line.split('|')
        movie_list[int(line[0])] = line[1]
    movie_file.close()


    G = Graph()

    reverse = {v:k for k, v in actors_list.items()}

    for movie in movie_actors_list.keys():
        for actor1 in movie_actors_list[movie]:
            for actor2 in movie_actors_list[movie]:
                if actor1 != actor2:
                    G.add_vertex(actor1)
                    G.add_vertex(actor2)
                    G.add_edge(actor1, actor2, movie)

    print("To quit the program, type return in answer to a question.")

    # repeat until the user inputs "return"
    while True:
        actor = input("Enter the name of an actor: ")
        if actor.lower() == "return":
            print("Finishing the program")
            break
        # if the user put the wrong name, notice that the name was wrong
        if actor not in actors_list.values():
            print("Wrong name. Enter again.\n")
            continue
        # getting the actors' ID based on their name
        actorID = reverse[actor]
        KB = reverse["Kevin Bacon"]

        # result for BFS
        result = BFS(G, KB, actorID)

        print("{0}'s number is {1}".format(actor, G.get_distance(actorID)))
        for i in range(G.get_distance(actorID), 0, -1):
            print("{0} appeared in {1} with {2}".format(actors_list[result[i].get_ID()], movie_list[result[i].get_weight(result[i-1])], actors_list[result[i-1].get_ID()]))
        print()


if __name__ == "__main__":
    main()