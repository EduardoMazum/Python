V = int(input("Ingrese el arreglo 20 a 60 "))
def intervalo(b):

	p = range(20, 60)
	for i in range(len(p)):
		if b < len(p):
			if i <= b:
				print (i, " ", p[i])
		else:
			print ("No esta dentro del rango ")
intervalo(V)
input()