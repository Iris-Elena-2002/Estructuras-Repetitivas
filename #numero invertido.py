#numero invertido

numero = int(input("Ingresa un número entero: "))

es_negativo = numero < 0

numero = abs(numero)

numero_invertido = 0

while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10

if es_negativo:
    numero_invertido *= -1

print(f"El número invertido es: {numero_invertido}")
