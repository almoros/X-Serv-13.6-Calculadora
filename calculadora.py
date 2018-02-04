#!/usr/bin/python3

import sys

def add(num1, num2):
	return num1 + num2

def sub(num1, num2):
	return num1 - num2
	
def mul(num1, num2):
	return num1 * num2
	
def div(num1, num2):
	return num1 / num2

operation = str(sys.argv[1])

try:

	num1 = int(sys.argv[2])
	num2 = int(sys.argv[3])
	
except ValueError:
	print("Valor erróneo, por favor introduce solamente números enteros")
	exit()
except IndexError:
	print("Formato no válido, utilice: python3 calculadora.py 'operación' 'número 1' 'número 2'")
	exit()

if operation == "sumar":
	print(add(num1,num2))
			
elif operation == "restar":
	print(sub(num1,num2))

			
elif operation == "multiplicar":
	print(mul(num1,num2))

elif operation == "dividir":
	try:
		print(div(num1,num2))
	except ZeroDivisionError:
		print("No se puede dividir por cero")
			
else:
	print("Esa función no esta definida, utilice los comandos:\nsumar, restar multiplicar o dividir")

	
