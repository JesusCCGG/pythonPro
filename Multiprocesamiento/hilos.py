import threading
import time

def tarea1():
    print("Iniciando tarea 1...")
    time.sleep(2)  # Simulamos una tarea que tarda 2 segundos en completarse
    print("Tarea 1 completada.")

def tarea2():
    print("Iniciando tarea 2...")
    time.sleep(2)  # Simulamos una tarea que tarda 3 segundos en completarse
    print("Tarea 2 completada.")

# Creamos los hilos para ejecutar las tareas
hilo1 = threading.Thread(target=tarea1)
hilo2 = threading.Thread(target=tarea2)

# Iniciamos los hilos
hilo1.start()
hilo2.start()

# Esperamos a que ambos hilos terminen
hilo1.join()
hilo2.join()

print("Ambas tareas han finalizado.")
