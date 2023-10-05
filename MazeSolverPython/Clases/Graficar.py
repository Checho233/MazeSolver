import matplotlib.pyplot as plt
import numpy as np

def mostrar_soluciones(maze, soluciones):
    # Convierte el laberinto a un array de NumPy para facilitar la manipulación
    maze = np.array(maze)

    # Crea una nueva figura para cada solución
    for i, solucion in enumerate(soluciones):
        plt.figure(i)
        
        # Crea una copia del laberinto para no modificar el original
        maze_copy = np.copy(maze)
        
        # Marca el camino de la solución en el laberinto
        for x, y in solucion:
            if 0 <= y < len(maze_copy) and 0 <= x < len(maze_copy[0]):
                maze_copy[y][x] = 2

        # Muestra el laberinto
        plt.imshow(maze_copy, cmap='hot')
        plt.colorbar()

    # Muestra todas las figuras
    plt.show()


