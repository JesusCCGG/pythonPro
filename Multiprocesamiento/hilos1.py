import threading

def incrementar():
    global variable
    for _ in range(100000):
        variable += 1
    print("Incremento completado. Valor final:", variable)

def decrementar():
    global variable
    for _ in range(100000):
        variable -= 1
    print("Decremento completado. Valor final:", variable)

# Variable compartida por ambos hilos
variable = 0

# Creamos los hilos para ejecutar las tareas
hilo_incremento = threading.Thread(target=incrementar)
hilo_decremento = threading.Thread(target=decrementar)

# Iniciamos los hilos
hilo_incremento.start()
hilo_decremento.start()

# Esperamos a que ambos hilos terminen
hilo_incremento.join()
hilo_decremento.join()

print("Ambas tareas han finalizado. Valor final de la variable:", variable)
