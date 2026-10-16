"Ejercicio3"
import threading

def tareaC(nombre): 
    print("Hola ",nombre)

hiloC= threading.Thread(target=tareaC,args=("Jennyfer",))
hiloC.start() 


