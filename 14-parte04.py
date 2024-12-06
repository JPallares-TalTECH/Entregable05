# Calculadora
def calculadora(a,b,c):
    if c == "suma":
        return (a+b)
    elif c == "resta":
        return (a-b)
    elif c == "multi":
        return (a*b)
    elif c == "divi":
        if b != 0:
            return (a/b)
        else:
            print("¡Error!: La división por cero no está definida.")
    else:
        print("Operación no válida.")

print("Calculadora básica:")
n1 = float(input("Digita el primer número: "))
n2 = float(input("Digita el segundo número: "))
opc = input("Digita la operación a realizar (\"suma\", \"resta\", \"multi\", \"divi\"): ").lower()

print(f"Resultado: {calculadora(n1, n2, opc)}")

# Adivinanza
import random
num_random, adivina = random.randint(1, 10), -1

print("Adivina el número entre 1 y 10")
while adivina != num_random:
    adivina = int(input("Adivina el número: "))
    if adivina < num_random:
        print(">> El número es mayor >>")
    elif adivina > num_random:
        print("< <El número es menor <<")
    else:
        print("¡Correcto! ¡¡Adivinaste el número!!")
