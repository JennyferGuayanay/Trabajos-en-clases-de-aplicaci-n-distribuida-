import threading
import time

def descargar(nombre, tamanio):
    print("Descargando", nombre, "(", tamanio, "MB)...")
    time.sleep(tamanio)
    print("Descarga completa:", nombre)

hiloA = threading.Thread(target=descargar, args=("archivo1.zip", 5))
hiloB = threading.Thread(target=descargar, args=("archivo2.mp4", 7))
hiloC = threading.Thread(target=descargar, args=("archivo3.pdf", 3))

hiloA.start()
hiloB.start()
hiloC.start()

hiloA.join()
hiloB.join()
hiloC.join()

print("Todas las descargas terminaron")
