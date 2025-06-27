#Problema 4
"""Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. """

#Solución
num = int(input("Ingrese un número entero: "))
sum_1_num = (num * (num + 1))//2
print(f'La suma de todos los enteros desde 1 hasta {num} es: {sum_1_num}')
