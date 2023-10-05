from Clases.MazeSolver import MazeSolver
from Clases.Control import Control
from Clases.Graficar import mostrar_soluciones
from game2dboard import * 
import csv
import time

class Main :
    def main():        
        file_read = csv.reader(open("archivo3.csv", encoding= 'utf-8-sig'),  delimiter=';')
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
            mazeSolver.solve(maze2, entrada[1], entrada[0], salida[1], salida[0])
            if mazeSolver.todas_las_soluciones:
                print("Se encontraron las siguientes soluciones:")
                for solucion in mazeSolver.todas_las_soluciones:
                    print(solucion)
                    coordenadas = solucion
                
                    x, y = zip(*coordenadas)
                    
                    b = Board(len(maze2[0]), len(maze2))
                    
                    b.title = "Laberinto"
                    b.cell_size = 60       
                    b.cell_color = "dark green"
                    
                    '''def  cambiar():
                        for i, j in zip(x, y):
                            b[i][j] = "cuadro" 
                        
                            
                    b.on_start = cambiar
                    
                    b.show()'''
            else :
                print("No se encontró una solución")
        else:
            print("El laberinto no cumple con las condiciones.")
            
        
        soluciones = mazeSolver.todas_las_soluciones
        
        mostrar_soluciones(maze2, soluciones)
                        
if __name__ == '__main__':
    Main.main()