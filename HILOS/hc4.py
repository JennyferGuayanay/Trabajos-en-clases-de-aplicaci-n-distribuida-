"Ejercicio5"
import threading

def tareaA():
    for i in range(5):
        print("Hilo A:A", i)

def tareaB():
    for i in range(5):
        print("Hilo B:B", i)

def tareaC(nombre, curso):
    print("Hilo", nombre, curso)

def tarea(hilo):
    for i in range(5):
        print("Hilo", hilo, i)


hiloA = threading.Thread(target=tareaA)
hiloA.start()
hiloA.join()

hiloB = threading.Thread(target=tareaB)
hiloB.start()
hiloB.join()

hiloC = threading.Thread(target=tareaC, args=("C", "Python"))
hiloC.start()
hiloC.join()

hiloD = threading.Thread(target=tarea, args=("D",))
hiloD.start()
hiloD.join()

for i in range(5):
    print("Soy hilo principal", i)
