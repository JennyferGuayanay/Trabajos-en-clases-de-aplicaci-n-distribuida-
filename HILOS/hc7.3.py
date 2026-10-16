import threading

contador = 0
bloqueo = threading.Lock()

def asignar_turno(cliente):
    global contador

    with bloqueo:
        contador += 1
        turno = contador
        print("Turno", turno, "asignado.")

    print("Cliente", cliente, ": Recibí el turno", turno)

hiloA = threading.Thread(target=asignar_turno, args=(1,))
hiloB = threading.Thread(target=asignar_turno, args=(2,))
hiloC = threading.Thread(target=asignar_turno, args=(3,))

hiloA.start()
hiloB.start()
hiloC.start()

hiloA.join()
hiloB.join()
hiloC.join()

print("Todos los turnos fueron asignados")