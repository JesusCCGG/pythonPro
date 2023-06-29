#Conexion de python con BD mysql
import mysql.connector
import sys


cnn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            db='Computadora'
        )
cur=cnn.cursor()
print("\n")
def comprobar():
    print("Conexion correcta ",cnn)

def consultar():
    cur.execute("select * from laptop")
    datos=cur.fetchall()
    for fila in datos:
        print(fila)

def insertar():
    
    modelo=str(input("Modelo: "))
    print(modelo)

    procesador=str(input("procesador: "))
    print(procesador)

    ram=str(input("ram: "))
    print(ram)

    tamPantalla=str(input("tamPantalla: "))
    print(tamPantalla)

    precio=str(input("precio: "))
    print(precio)

    velProcesador=str(input("velProcesador: "))
    print(velProcesador)

    cur.execute("insert into Laptop(modelo,  procesador, ram, tamPantalla, precio, velProcesador) values('"+modelo+"','"+procesador+"','"+ram+"','"+tamPantalla+"','"+precio+"','"+velProcesador+"')")

    cnn.commit()
def borrar():
    print("In progress")

def actualizar():
    print("In progress")
def salir():
    print("Bye")
    sys.exit(1)
   
def error():

    print('error')

switch_funcion = {
    1: comprobar,
	2: insertar,
	3: consultar,
    4: borrar,
    5: actualizar,
    6: salir,
	
}

opt = int(input("1.Comprobar conexion a la BD\n2.Insertar\n3.Consultar\n4.Borrar\n5.Actualizar\n\tIngresa una opcion: "))
switch_funcion.get(opt, error)()

cur.close()
cnn.close()
