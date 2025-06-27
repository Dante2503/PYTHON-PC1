#Problema 2
"""En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina."""

#Solución
costo_cena = int(input("Ingrese el costo total de su cena: "))
porc_propina = float(input("Porcentaje de propina (mayor o igual al 15%): "))
propina = porc_propina * (costo_cena/100)
print(f"La propina que debe dejar es: ${propina:.2f}")