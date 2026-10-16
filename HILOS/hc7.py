import threading
import time

def mensaje(cliente):
    print("Atendiendo", cliente)
    time.sleep(2)
    print("Cliente", cliente, "atendido")

hiloA = threading.Thread(target=mensaje, args=(" 1",))
hiloA.start()
hiloB = threading.Thread(target=mensaje, args=(" 2",))
hiloB.start()
