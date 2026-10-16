import threading

bloqueo = threading.Lock()

def imprimir(numero):
    with bloqueo:
        print(f"Hilo {numero} esta imprimientdo us conjunto de numeros")
        for i in range(5):
            print("Hilo", numero, "número:", i)
        print("Hilo", numero, "ha terminado.")

hilos = []

for i in range(1, 12):
    hilo = threading.Thread(target=imprimir, args=(i,))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Hilos terminados")

