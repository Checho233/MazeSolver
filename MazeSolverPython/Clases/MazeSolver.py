class MazeSolver :
    def __init__(self):
        self.todas_las_soluciones = []

    def solve(self, maze, startX, startY, endX, endY, path=None):
        if path is None:
            path = []

        # Añade la posición actual al camino
        path.append((startY, startX))

        # Verifica si hemos llegado a la salida
        if startX == endX and startY == endY:
            self.todas_las_soluciones.append(path)
            return

        rows = len(maze)
        cols = len(maze[0])

        # Verificar si estamos fuera de los limites o en una celda bloqueada
        if startX < 0 or startX >= cols or startY < 0 or startY >= rows or maze[startY][startX] == 1:
            return

        # Marcar la celda como visitada
        maze[startY][startX] = 1

        # Explorar las cuatro direcciones posibles
        self.solve(maze, startX+1, startY, endX, endY, path.copy())
        self.solve(maze, startX-1, startY, endX, endY, path.copy())
        self.solve(maze, startX, startY+1, endX, endY, path.copy())
        self.solve(maze, startX, startY-1, endX, endY, path.copy())

        # Si ninguna direccion lleva a la solución, desmarcar la celda
        maze[startY][startX] = 0
