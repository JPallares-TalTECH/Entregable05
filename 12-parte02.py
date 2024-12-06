# Número par
numero = int(input("Introduce el número para validar si es par o impar: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

# for: imprime los cuadrados de los números de la lista
lista = [3, 6, 9, 12, 18, 20]
print("\nLista: ",lista)
for n in lista:
    print("El cuadrado de ",n," es: ",n*n)

# while: Solicita ingresar un dato hasta que el usuario introduzca un cero (0)
caracter = ""
while caracter != "0":
    caracter = input("Digita un caracter alfanumerico ('0' para salir): ")
    print("Has introducido: ",caracter)
