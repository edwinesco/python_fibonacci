# Programa que implementa la funcion Fibonacci usando "generadores" para
# optimiza el uso de la memoria

""" Un generador en Python es una función especial que produce una secuencia 
de valores de manera eficiente y bajo demanda. A diferencia de las listas 
o tuplas, que almacenan todos los valores en memoria, los generadores 
generan los valores uno a uno a medida que se solicitan 

Los generadores se definen como funciones normales, pero en lugar de usar 
return, utilizan la palabra clave yield

"""

# Uso de la funcion "yield" que es igual que el return pero en lugar
# de terminar la ejecucion pausa y guarda su estado paar usarse luego

def fibonacci():
	a, b = 0, 1
	while True:
		yield a	# La función no se detiene aquí; simplemente pausa su ejecución y espera a que se solicite el siguiente valor.
		a, b = b, a + b

generador_fibo = fibonacci()

for _ in range(10):	#El guion bajo (_) se utiliza en este caso como una convención para indicar que no estamos interesados en el valor de la variable en el bucle for.
	print(next(generador_fibo))