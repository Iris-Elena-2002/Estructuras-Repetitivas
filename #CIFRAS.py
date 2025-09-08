#CIFRAS

num=int(input("Ingresa un numero..."))
contador=0

if num==0:
  contador=1

else:
 while num>0:
   num%10==0
   contador = contador+1

print("El numero", num, "tiene", contador, "cifras")