# Palindromos sin espacios y sin diferenciar entre mayusculas y minusculas
def reverse(texto):
    rev = ""
    for char in texto:
        if (char != " "):
            rev = char+rev
    return rev


def sinSpc(texto):
    org = ""
    for char in texto:
        if (char != " "):
            org = org+char
    return org


def comparador(texto, reverso):
   return True if texto == reverso else False #operador ternario
    # if texto == reverso:
    #     return True
    # else:
    #     return False


textoOriginal = input("Ingresa un string para comprobar si es un palindromo: ")

textoMinsc = textoOriginal.lower()
reverso = reverse(textoMinsc)
original = sinSpc(textoMinsc)

print("Texto ingresado: ", original, "\nTexto al reves: ", reverso,
      "\n -Palindromo: ", comparador(reverso, original), "-")
