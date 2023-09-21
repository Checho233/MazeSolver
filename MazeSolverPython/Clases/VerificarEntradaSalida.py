class VerificarEntradaSalida:
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