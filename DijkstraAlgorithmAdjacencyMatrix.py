import sys

class DijkstraAlgorithm:

    def __init__(self,adjacency_matrix, start_node):

        self.adjacency_matrix = adjacency_matrix
        self.start_node = start_node
        self.v = len(adjacency_matrix)
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.distances[start_node] = 0

    #Esta función encontrará el nodo con la menor distancia
    def get_min_vertex(self):

        min_vertex_value = sys.maxsize
        min_vertex_index = 0

        #Busqueda lienar con una complejidad de O(v)
        #Por esta razón se prefiere utilizar heaps 
        for index in range(self.v):
            if not self.visited[index] and self.distances[index] < min_vertex_value:
                min_vertex_value = self.distances[index]
                min_vertex_index = index
        
        return min_vertex_index

    def calculate(self):

        #Consideramos todos los items en O(v)
        for vertex in range(self.v):
            actual_vertex = self.get_min_vertex()
            print('Considerando el nodo %s' % actual_vertex)
            self.visited[actual_vertex] = True        

            #Aquí nuevamente tenemos una complejidad de O(v) por lo que la complejidad total es de O(v^2)
            for other_vertex in range(self.v):
                #Si hay una conexión entre los dos nodos entonces
                if self.adjacency_matrix[actual_vertex][other_vertex] > 0:
                    #Revisamos si hay un camino más corto desde el vértice(nodo) actual al otro vertice
                    if self.distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex] < self.distances[other_vertex]:
                        self.distances[other_vertex] = self.distances[actual_vertex] + self.adjacency_matrix[actual_vertex][other_vertex]

    def print_distances(self):
        print(self.distances)

if __name__ == '__main__':

    m = [[0, 7, 5, 2, 0, 0],
         [7, 0, 0, 0, 3, 8],
         [5, 0, 0, 10, 4, 0],
         [2, 0, 10, 0, 0, 2],
         [0, 3, 4, 0, 0, 6],
         [0, 8, 0, 2, 6, 0]]

    algorithm = DijkstraAlgorithm(m, 0)
    algorithm.calculate()
    algorithm.print_distances()
