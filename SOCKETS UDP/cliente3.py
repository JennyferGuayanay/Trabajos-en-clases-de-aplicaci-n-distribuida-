
import socket
import json
import time

#Configuracion de socker del cliente
socketClient=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
direccionServer=("localhost",5000)

while True: 
    opciones=input ("Elija una opcion")
    print ("1: Registar usuario")
    print ("2: Consultar usuario por cedula")
    print ("3: Recargar saldo")

    if opciones== "1": 
        print ("Ingrese el usuario usuario")
        nombre=input("Nombre: ")
        cedula=input("Numero de Cedula: ")
        correo=input("Correo electronico: ")
        telefono=input("Numero de telefono: ")

        mensaje = {
            "opcion": opciones,
            "nombre":nombre, 
            "cedula":cedula,
            "correo":correo,
            "telefono":telefono
        }

    socketClient.sendto(json.dumps(mensaje).encode(),direccionServer)
    data, direccion = socketClient.recvfrom(1024)
    mensaje=data.decode()
    print(mensaje)

if opciones=="2":
    print()
    
socketClient.close()
