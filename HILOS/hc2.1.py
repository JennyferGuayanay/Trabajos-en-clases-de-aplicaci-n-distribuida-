"Ejercicio2.1"
import threading
def tareaA():
    for i in range (5):
        print ("Hilo A:A",i)

def tareaB():
    for i in range (5):
        print ("Hilo B:B",i)

hiloA= threading.Thread(target=tareaA)
hiloA.start() 
hiloA.join()
hiloB= threading.Thread(target=tareaB)
hiloB.start() 
hiloB.join()

for i in range (5):
    print("Soy hilo principal",i)

    