def buscar_camino_mas_corto(maze, source, dest):
    if maze[source[0]][source[1]] != 'S' or maze[dest[0]][dest[1]] != 'D':
        return None  # las celdas de origen y destino deben ser válidas
    rows, cols = len(maze), len(maze[0])
    visited = set()  # conjunto de celdas visitadas
    queue = [(source, [source])]  # cola de celdas por visitar, con el camino recorrido hasta cada celda
    while queue:
        curr, path = queue.pop(0)
        if curr == dest:
            return path  # se ha encontrado el destino, se devuelve el camino recorrido hasta aquí
        visited.add(curr)
        for r, c in [(curr[0]-1, curr[1]), (curr[0], curr[1]+1), (curr[0]+1, curr[1]), (curr[0], curr[1]-1)]:
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] != '0' and (r, c) not in visited:
                queue.append(((r, c), path + [(r, c)]))  # se agrega la celda a la cola, con el camino recorrido hasta aquí
                visited.add((r, c))
    return None  # no se ha encontrado un camino válido desde la fuente hasta el destino


if __name__ == '__main__':

    maze = [
   ["S", 0, 1, 1, 1],
   [1, 1, 1, 0, 1],
   [0, 0, 0, 1, 1],
   [1, 1, 1, 1, 0],
   [1, 0, 0, 0, 0],
   [1, 1, 1, 1, "D"]
    ]

    source = (0,0)
    dest = (5,4)
    camino = buscar_camino_mas_corto(maze,source,dest)

    print(camino)