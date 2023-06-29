n1=input("Ingresa un numero: ")
while n1 != 'salir' or n2 != 'salir':
    op=input("Ingresa una operacion: ")
    n2=input("Ingresa otro un numero: ")
    if str(n2)=='salir':
            break
    else:
        if op == "sum":
            res=int(n1)+int(n2)
        elif op == "res":
            res=int(n1)-int(n2)
        elif op == "div":
            res=int(n1)/int(n2)
        elif op == "mul":
            res=int(n1)*int(n2)
        n1=res   
        print(res)
        
    



    
