"Ejercicio8"

import time
import threading
empresa = {
    "S001": ["Ventas", 4],
    "S002": ["Inventarios", 1],
    "S003": ["Contabilidad", 5],
    "S004": ["Compras", 3],
    "S005": ["Logistica", 4]
}

def atencion(codigo):
    print("Atendiendo", codigo, empresa[codigo][0])
    time.sleep(empresa[codigo][1])

for clave,valor in empresa.items():
    atencion(clave)

inicio=time.perf_counter() # reloj interno 
hilos=[]
for clave,valor in empresa.items():
    hilo = threading.Thread(target=atencion, args=(clave,))
    hilo.start()
    hilos.append(hilo)

for i in hilos:
    i.join()

tiempo_concurrencia=time.perf_counter()-inicio
print("Tiempo con hilos", tiempo_concurrencia)
