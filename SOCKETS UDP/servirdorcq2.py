import socket

socketServer=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socketServer.bind(("localhost", 5000))  

while True:
    data, addr = socketServer.recvfrom(1024)
    mensaje=data.decode()
    print(mensaje, "de", addr)

    mensaje2="Hola soy el servidor"
    socketServer.sendto(mensaje2.encode(),addr)