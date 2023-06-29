#ejemplos de uso del fstring
variable = "Valor"
print(f"Valor = {variable}")
print(f"{variable = }")

#sep para print
a = 4
b = 3
c = 7
print(a, b, c, sep="-")

#end para print
for i in range(4):
    print(i, end="-")

#creacion y esritura en archivos con print
def archivos():
    with open("hola_mundo.txt","w") as archivo:
        print("Hola mundo",file=archivo)
#archivos()