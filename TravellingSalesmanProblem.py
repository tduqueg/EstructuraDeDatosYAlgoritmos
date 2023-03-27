
class TravellingSalesmanProblem:

    def __init__(self, graph):

        #El Grafo G(V,E)
        self.graph = graph
        #n es el numero de V vertices en el grafo G(V,E)
        self.n = len(graph)
        #Consideramos si ya hemos visitado los nodos
        self.visited = [False for _ in range(self.n)]
        #Empezamos con el primer vértice aunque podemos empezar con cualquier vertice aleatorio
        #Debido a que es un ciclo
        self.visited[0] = True
        #Recolectamos todos los ciclos Hamiltonianos
        #Tenemos que seleccionar el minimo
        self.hamiltonian_cycles = []
        #Llevamos la cuenta de cuales vertices están incluidos en el ciclo
        self.path = [0 for _ in range(self.n)]

    def is_valid(self, vertex, actual_position):
        
        #tenemos que revisar si el nodo dado ya lo hemos visitado
        if self.visited[vertex]:
            
            return False

        #Tenemos que revisar si hay una conexión entre esos vertices
        if self.graph[actual_position][vertex] == 0:

            return False
        
        return True
    
    def tsp(self, actual_position, counter, cost):

        #Tenemos que considerar todos los nodos i en el grafo
        #y si el último nodo puede ser conectado al primero (Ciclo)
        if counter == self.n and self.graph[actual_position][0]:
           
            self.path.append(0)
            print(self.path)
            self.hamiltonian_cycles.append([ cost + self.graph[actual_position][0]])
            self.path.pop()
            return
        
        for i in range(self.n):

            if self.is_valid(i, actual_position):

                self.path[counter] = i
                self.visited[i] = True

                #Tenemos que llamar la función recursivamente
                self.tsp(i, counter +1 , cost + self.graph[actual_position][i])

                #Debemos hacer Bactraking
                self.visited[i] = False

if __name__ == '__main__':

    g = [[0, 1, 0, 2, 0],
         [1, 0, 1, 0, 2],
         [0, 1, 0, 3, 1],
         [2, 0, 3, 0, 1],
         [0, 2, 1, 1, 0]]

    tsp = TravellingSalesmanProblem(g)
    #Emepazos por el vertice representado con el indice 0
    #El contador es 1 porque es la primera iteración
    #El costo es de 0
    tsp.tsp(0, 1, 0)
    print(min(tsp.hamiltonian_cycles))



