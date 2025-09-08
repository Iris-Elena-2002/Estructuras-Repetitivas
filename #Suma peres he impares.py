#Suma peres he impares

i=int(input("Ingresa un numero..."))
suma1=0
suma2=0

for i in range (1,i+1):
    if(i/2== 0):
     suma1 =suma1+1
    elif(i/3== 0):
     suma2 =suma2+1

print("La suma de los numeros pares de 0 hasta n es:", suma1) 
print("La suma de los numeros impares de 0 hasta n es:", suma2)