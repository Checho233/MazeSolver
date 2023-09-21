class Entrada_Salida:
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