class MazeSolver :
    def solve(self, maze, startX, startY, endX, endY) :
        rows = len(maze)
        cols = len(maze[0])
        
        #Verificar si estamos fuera de los limites o en una celda bloqueada
        if startX < 0 or startX >= cols or startY < 0 or startY >= rows or maze[startY][startX] == 1 :
            return False
        
        #Verifica si hemos llegado a la salida
        if startX == endX and startY == endY :
            return True
        
        #Marcar la celda como visitada
        maze[startY][startX] = 1
        print(f"Marcar la posición {startY} , {startX}")
        
        #Explorar las cuatro direcciones posibles
        if (self.solve(maze, startX+1, startY, endX, endY) or 
            self.solve(maze, startX-1, startY, endX, endY) or 
            self.solve(maze, startX, startY+1, endX, endY) or 
            self.solve(maze, startX, startY-1, endX, endY)) :
                return True
            
        #Si ninguna direccion lleva a la solución, desmarcar la celda
        maze[startY][startX] = 0

        print("Marcar la posición " + startY + ", " + startX)

        return False
        