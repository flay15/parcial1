# Manipulación de cadenas
cadena = input("Ingresa una cadena de texto: ")

minusculas = cadena.lower()
num_palabras = len(cadena.split())
contiene_programacion = "programación" in cadena

print(f"Cadena en minúsculas: {minusculas}")
print(f"Número de palabras: {num_palabras}")
print(f"¿La cadena contiene 'programación'?: {contiene_programacion}")
