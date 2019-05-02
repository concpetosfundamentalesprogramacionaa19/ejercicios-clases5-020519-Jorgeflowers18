"""
	file: run2.py
	autor: @Jorgeflowers18

"""

"""
nota mayor o igual a 18: sobresaliente

nota mayor o igual a 16 y menor a 18: muy buena

nota mayor o igual a 13 y menor a 16: buena

nota menor a 13: insuficiente

"""


from misvariables import *

nota = int(input("Ingrese la primera nota 1: "))
# nota2 = int(input("Ingrese la segunda nota 2: "))

"""
nota = int(nota)
nota2 = int(nota2)
"""

if nota >=18:
	print("%s - nota %d" % ("Sobresaliente", nota))
else:
	if (nota >= 16) and (nota < 18):
		print("%s - nota %d" % ("Muy buena", nota))
	else:
		if (nota >= 13) and (nota < 16):
			print("%s - nota %d" % ("Muy buena", nota))
		else:
			print("%s - nota %d" % ("Insuficiente", nota))
"""
if nota >=18:
	print("%s - %d" % (mensaje, nota))
else:
	print("%s - %d" % (mensaje2, nota))

if nota2 >=18:
	print("%s - %d" % (mensaje, nota2))
else:
	print("%s - %d" % (mensaje2, nota2))
"""






















