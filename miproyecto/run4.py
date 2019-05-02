"""
	file: run4.py
	autor: @Jorgeflowers18

"""

"""
	Deseamos obtener el costo de una carrera universitaria, 
	el valor promedio de cada ciclo es de 1200 dolares, 
	el valor promedio del seguro educativo por ciclo 
	es de 100 dolares si la edad del estudiante es 
	menor o igual a 20 caso contrario será de $150 si 
	el estudiante tiene una modalidad a distancia, 
	el número de ciclos a seguir es 10, caso contrario 
	deberá seguir 8 ciclos.

"""

# Se pide las variables

print("Bienvenido al sistema de cálculo de costo de carrera de la UTPL")

modalidad = input("Ingrese por favor la modalidad que desea (escriba distancia o presencial: ")

edad = int(input("Ingrese por favor su edad: "))

# Utilización de operaciones anidadas
costo = 1200

costm = 0

seguro = 0


if (modalidad == "presencial"):
	costm = 8 * costo
	if edad <= 20:
		seguro = 8 * 100
		costo = costm + seguro
	else:
		seguro = 8 * 150
		costo = costm + seguro

else:
		costm = 10 * costo
		if edad <= 20:
			seguro = 10 * 100
			costo = costm + seguro
		else:
			seguro = 10 * 150
			costo = costm + seguro

# Se presenta el costo final

print("El costo de su carrera universitaria es: ", costo)



















