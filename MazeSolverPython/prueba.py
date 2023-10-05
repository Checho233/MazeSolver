# Definir la clase MazeSolver
class MazeSolver:

    # Definir el método constructor
    def __init__(self, laberinto, entrada, salida):
        # Guardar el laberinto como un atributo de la clase
        self.laberinto = laberinto
        # Obtener las dimensiones del laberinto
        self.filas = len(laberinto)
        self.columnas = len(laberinto[0])
        # Guardar las coordenadas de la entrada y la salida como atributos de la clase
        self.entrada = entrada
        self.salida = salida
        # Definir las direcciones posibles: arriba, abajo, izquierda y derecha (sin diagonales)
        self.direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # Crear una matriz para guardar las celdas visitadas
        self.visitados = [[False for j in range(self.columnas)] for i in range(self.filas)]

    # Definir el método que verifica si una celda es válida y no está visitada
    def es_valida(self, i, j):
        return (0 <= i < self.filas and 0 <= j < self.columnas and self.laberinto[i][j] == 0 and not self.visitados[i][j])

    # Definir el método que encuentra todos los caminos posibles usando backtracking
    def encontrar_caminos(self, i, j, camino):
        # Caso base: si se llega a la salida usando las coordenadas guardadas
        if i == self.salida[0] and j == self.salida[1]:
            # Imprimir el camino encontrado
            print(camino + [(i,j)])
            # Terminar la recursión
            return
        # Marcar la celda actual como visitada
        self.visitados[i][j] = True
        # Agregar la celda actual al camino
        camino.append((i,j))
        # Recorrer las cuatro direcciones posibles
        for di, dj in self.direcciones:
            # Calcular las coordenadas de la celda vecina
            ni = i + di
            nj = j + dj
            # Si la celda vecina es válida y no está visitada
            if self.es_valida(ni, nj):
                # Llamar al método recursivamente con la nueva celda
                self.encontrar_caminos(ni, nj, camino)
        # Quitar la celda actual del camino (backtracking)
        camino.pop()
        # Desmarcar la celda actual como visitada
        self.visitados[i][j] = False

# Definir el laberinto como una matriz de 0 y 1
laberinto = [
    [0, 1, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

# Definir las coordenadas de la entrada y la salida (fila, columna)
entrada = (4, 0)
salida = (2, 4)

# Crear una instancia de la clase MazeSolver con el laberinto y las coordenadas dadas
solver = MazeSolver(laberinto, entrada, salida)

# Crear una lista para guardar el camino actual
camino = []

# Llamar al método con la celda de entrada
solver.encontrar_caminos(entrada[0], entrada[1], camino)

# Salida:
# [(4, 0), (3, 0), (2, 0), (2, 2), (2, 3), (2, 4)]
# [(4, 0), (3, 0), (3, 3), (2, 3), (2, 4)]