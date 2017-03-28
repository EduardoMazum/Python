import math
i = float(input("ingrese cateto 1: \n"))
o = float(input("ingrese cateto 2: \n"))

def hipotenusa (i, o):
	Hp = math.sqrt(( i*i + o*o))
	print("La hipotenusa es :")
	print(Hp)
	
hipotenusa(i, o)

input()

