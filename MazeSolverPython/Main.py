from Clases.MazeSolver import MazeSolver
from Clases.Control import Control
import tkinter
from game2dboard import * 
import csv

class Main :
    def main():        
        file_read = csv.reader(open("archivo.csv", encoding= 'utf-8-sig'),  delimiter=';')
        maze = list(file_read)
        aux = [[int(i) for i in row] for row in maze]
        maze2 = aux
 
        res = Control.find_entrance_exit(maze2)
        entrada, salida = res
        cuadrado = Control.check_zero_squares(maze2)
        cuadradoUnos = Control.check_one_squares(maze2)
        verificar_entrada_salida = Control.check_one_exit(maze2)
        
        mazeSolver = MazeSolver()
        
        if verificar_entrada_salida == True and cuadrado == False and cuadradoUnos == False:
                if mazeSolver.solve(maze2, entrada[1], entrada[0], salida[1], salida[0]):
                    print("Se encontro una solución")
                    coordenadas = MazeSolver.coordenadas()
                
                    x = coordenadas[0]
                    y = coordenadas[1]
                    x.append(salida[1])
                    y.append(salida[0])
                    
                    b = Board(len(maze2[0]), len(maze2))
                    
                    b.title = "Laberinto"
                    b.cell_size = 60       
                    b.cell_color = "dark green"
                    
                    def  cambiar():
                        for i, j in zip(x, y):
                            b[i][j] = "cuadro" 
                        
                            
                    b.on_start = cambiar
                    
                    b.show()
                else :
                    print("No se encontro una solución")
        else:
            print("El laberinto no cumple con las condiciones.")
                        
            
        '''
        if verificar_entrada_salida:
            print("Solo hay una entrada y una salida")
            
        if not cuadrado:
            print("No hay ningun cuadrado en el laberinto")
        elif cuadrado:
            print("Si hay cuadrados de ceros.")
        if not cuadradoUnos:
            print("No hay ningun cuadrado de unos")
        elif cuadradoUnos:
            print("Si hay cuadrados de unos")
        '''
if __name__ == '__main__':
    Main.main()