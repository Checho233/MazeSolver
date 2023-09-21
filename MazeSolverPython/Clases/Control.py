class Control:
    def check_one_exit (maze):
            # Obtener el número de filas y columnas del array
            rows = len (maze)
            cols = len (maze [0])

            # Inicializar un contador de ceros en el borde
            zeros = 0

            # Recorrer la primera y la última fila del array
            for i in [0, rows - 1]:
                for j in range (cols):
                    # Si el elemento actual es cero, incrementar el contador
                    if maze [i] [j] == 0:
                        zeros += 1

            # Recorrer la primera y la última columna del array, sin contar las esquinas
            for i in range (1, rows - 1):
                for j in [0, cols - 1]:
                    # Si el elemento actual es cero, incrementar el contador
                    if maze [i] [j] == 0:
                        zeros += 1

            # Verificar si el contador es igual a dos
            if zeros == 2:
                return True # Hay una sola salida
            else:
                return False # Hay más de una salida o ninguna
    
    
    def check_zero_squares (maze):
        # Obtener el número de filas y columnas de la matriz
            rows = len (maze)
            cols = len (maze [0])

            # Crear una matriz auxiliar del mismo tamaño que maze
            # Cada elemento de esta matriz representa el tamaño del cuadrado de ceros
            # que termina en esa posición
            aux = [ [0] * cols for _ in range (rows)]

            # Recorrer la matriz maze por filas y columnas
            for i in range (rows):
                for j in range (cols):
                    # Si el elemento actual es cero, entonces actualizar el elemento correspondiente en aux
                    if maze [i] [j] == 0:
                        # El tamaño del cuadrado de ceros es el mínimo entre el elemento superior, el izquierdo y el diagonal superior izquierdo, más uno
                        aux [i] [j] = 1 + min (aux [i-1] [j], aux [i] [j-1], aux [i-1] [j-1])
                        # Si el tamaño es mayor que uno, entonces hay un cuadrado de ceros en la matriz
                        if aux [i] [j] > 1:
                            return True

            # Si se recorrió toda la matriz sin encontrar un cuadrado de ceros, entonces retornar False
            return False
        
    def check_one_squares (maze):
        # Obtener el número de filas y columnas de la matriz
            rows = len (maze)
            cols = len (maze [0])

            # Crear una matriz auxiliar del mismo tamaño que maze
            # Cada elemento de esta matriz representa el tamaño del cuadrado de ceros
            # que termina en esa posición
            aux = [ [0] * cols for _ in range (rows)]

            # Recorrer la matriz maze por filas y columnas
            for i in range (rows):
                for j in range (cols):
                    # Si el elemento actual es cero, entonces actualizar el elemento correspondiente en aux
                    if maze [i] [j] == 1:
                        # El tamaño del cuadrado de ceros es el mínimo entre el elemento superior, el izquierdo y el diagonal superior izquierdo, más uno
                        aux [i] [j] = 1 + min (aux [i-1] [j], aux [i] [j-1], aux [i-1] [j-1])
                        # Si el tamaño es mayor que uno, entonces hay un cuadrado de ceros en la matriz
                        if aux [i] [j] > 1:
                            return True

            # Si se recorrió toda la matriz sin encontrar un cuadrado de ceros, entonces retornar False
            return False

    def find_entrance_exit (maze):
            # Obtener el número de filas y columnas del array
            rows = len (maze)
            cols = len (maze [0])

            # Inicializar las variables para almacenar los índices de la entrada y la salida
            entrance = None
            exit = None

            # Recorrer la primera y la última fila del array
            for i in [0, rows - 1]:
                for j in range (cols):
                    # Si el elemento actual es cero, verificar si es la entrada o la salida
                    if maze [i] [j] == 0:
                        # Si no hay entrada asignada, asignarla como la entrada
                        if entrance is None:
                            entrance = (i, j)
                        # Si hay entrada pero no hay salida asignada, asignarla como la salida
                        elif exit is None:
                            exit = (i, j)
                        # Si hay entrada y salida asignadas, significa que hay más de una salida, retornar None
                        else:
                            return None

            # Recorrer la primera y la última columna del array, sin contar las esquinas
            for i in range (1, rows - 1):
                for j in [0, cols - 1]:
                    # Si el elemento actual es cero, verificar si es la entrada o la salida
                    if maze [i] [j] == 0:
                        # Si no hay entrada asignada, asignarla como la entrada
                        if entrance is None:
                            entrance = (i, j)
                        # Si hay entrada pero no hay salida asignada, asignarla como la salida
                        elif exit is None:
                            exit = (i, j)
                        # Si hay entrada y salida asignadas, significa que hay más de una salida, retornar None
                        else:
                            return None

            # Verificar si se encontró una entrada y una salida válidas
            if entrance is not None and exit is not None:
                return entrance, exit # Retornar una tupla con las posiciones de entrada y salida
            else:
                return None # Retornar None si no se encontró una entrada y una salida válidas