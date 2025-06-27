#Problema 7
"""Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

#Solución
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: ")) 
#Menú
print("Seleccione una opción:")
print("1. Sumar")
print("2. Restar (primero menos segundo)")
print("3. Multiplicar")

opcion = input("Ingrese opción (1, 2 o 3): ")
#Condición
if opcion == "1":
    print(f"Resultado: {num1 + num2}")
elif opcion == "2":
    print(f"Resultado: {num1 - num2}")
elif opcion == "3":
    print(f"Resultado: {num1 * num2}")
else:
    print("Opción no válida") 

