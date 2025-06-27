#Problema 3
"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
último pedido y calcule el peso total del paquete que será enviado.
"""

#Solución
peso_payaso = 112
peso_muñeca = 75
num_payasos = int(input("Ingrese el número de payasos vendidos: "))
num_muñecas = int(input("Ingrese el número de muñecas vendidas: "))
peso_caja = (peso_payaso*num_payasos)+(peso_muñeca*num_muñecas)
print(f'En el último pedido se vendieron {num_payasos} payasos y {num_muñecas} muñecas pesando la caja un total de {peso_caja} g')
