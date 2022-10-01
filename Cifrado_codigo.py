#Codificacion Yazmin Reyes Barquera

abc ='abcdefghijklmnopkrstuvwxyz '
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
especiales = 'áéíóúü '


mensaje= input("Escribe el mensaje que quieres cifrar:        ")
llave = int(input("""Escribe la llave de cifrado:   """))

mcifrado= ""

for a in mensaje:
    if a in abc:
        pos = abc.index(a)
        newpos=(pos - llave)
        mcifrado += abc[newpos]
        
    elif a in ABC:
        pos = ABC.index(a)
        newpos=(pos - llave)
        mcifrado += ABC[newpos]

    break

print("-------------------------------------")
print("""Tu mensaje cifrado es:""",  mcifrado)
print("Gracias por utlizar este programa, tenga un lindo dia")


