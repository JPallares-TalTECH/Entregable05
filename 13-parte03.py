# Lista de nombres
lista = ["Veronica Berrio", "Humberto Covilla", "Manuel Romero", "Ana Correa"]
print("Estudiantes: ")
print("-----------")
for nombre in lista:
    print(nombre)
print("----------------------------------")

# Diccionario de contactos
info_contacto = {
    "Veronica Berrio": "vberrio@portalweb.com",
    "Humberto Covilla": "hcovilla@portalweb.com",
    "Manuel Romero": "mromero@portalweb.com",
    "Ana Correa": "acorrea@portalweb.com"
}
print("Nombre            Correo      ")
print("----------------------------------")
for nom, mail in info_contacto.items():
    print(f"{nom}      {mail}")
print("----------------------------------")

# Script, agregar elementos a una lista o actualizar un diccionario
nuevo = input("Introduce el nombre de un nuevo estudiante: ")
print("----------------------------------")
lista.append(nuevo)
print("Lista actualizada de estudiantes:")
print("--------------------------------")
for nombre in lista:
    print(nombre)
print("----------------------------------")

contacto = input("Introduce el nombre de un contacto para actualizar o agregar: ")
print("----------------------------------")
correo = input("Introduce el nuevo correo de este contacto: ")
print("----------------------------------")
info_contacto[contacto] = correo
print("¡¡Contacto actualizado!!")
print("----------------------------------")
print("Nombre                Correo      ")
print("----------------------------------")
for nom, mail in info_contacto.items():
    print(f"{nom}            {mail}")
print("----------------------------------")
