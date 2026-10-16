"Ejercicio2"
import threading
def tareaA():
    for i in range (5):
        print ("Hilo A:A",i)

def tareaB():
    for i in range (5):
        print ("Hilo B:B",i)

for i in range (5):
    print("Soy hilo principal")

hilo = threading.Thread(target=tareaA)
hilo.start() 

hilo = threading.Thread(target=tareaB)
hilo.start() 
