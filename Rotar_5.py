numero =[]
numero = input("Ingrese numeros : ")
z = input("Numero que Rotar: ")

def rotar (lista, z):
    guardar = list(lista)
    for i in range(len(lista)):

        if z<0:
            lista[i+z] = guardar[i]
        else:
            lista[i] = guardar[i-z]
        
rotar(numero, -z)

print (numero)
input()