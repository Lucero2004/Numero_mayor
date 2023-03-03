# Verifcar cual de los tres numeros es el mayor
print("------------------------------------------")
print("---------------NUMERO MAYOR DE TRES NUMEROS---------------")
print("------------------------------------------")

#input

A=int(input("Ingrese el primer numero: "))
B=int(input("Ingrese el segundo numero: "))
C=int(input("Ingrese el tercer numero: "))

#Procesing
if(A>B):
    Mayor=A
else:
    Mayor=B
if(C>Mayor):
    Mayor=C

#output
print("---------------------------------------")
print("El numero mayor es:" +str(Mayor))
print("----------------------------------------------")
