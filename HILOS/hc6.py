"Ejercicio6"

import threading

def tareaA():
    for i in range(5):
        print("Hilo A:A", i)

contador = 0
bloqueo = threading.Lock()

def aumentar(hilo):
    global contador
    for i in range(3):
        with bloqueo:
            aux = contador
            print(hilo, "lee", aux)
            aux = contador + 1
            contador = aux
            print(hilo, "escribe", contador)

hiloA = threading.Thread(target=aumentar, args=("hilo A",))
hiloA.start()

hiloB = threading.Thread(target=aumentar, args=("hilo B",))
hiloB.start()

for i in range(5):
    print("Soy hilo principal", i)

hiloA.join()
hiloB.join()

print("Contador final:", contador)
