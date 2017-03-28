def suma(n):
    if (n == 1):
        return 1
    else:
        res = (n**2) + suma(n-1)
        return res  

print(suma(num))

input()

  