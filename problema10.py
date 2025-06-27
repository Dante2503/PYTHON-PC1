#Problema 10
"""Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
encuentran en la posición 0, 4 y 5.
lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
Resultado esperado: ['Verde', 'Blanco', 'Negro']"""

#Solución
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
resultado = [lista[i] for i in range(len(lista)) if i not in (0, 4, 5)]
print(resultado)


