# Solicitar un número por teclado
numero = int(input("Ingrese un número: "))

# Crear un diccionario
diccionario = {i: i ** 3 for i in range(1, numero + 1)}

# Mostrar claves y valores
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")

#Ejercicio 2

# Crear un diccionario que almacene nombres de fruta como clave y su precio como valor
diccionarioFrutas = {
    "manzana": 1.20,
    "banana": 0.50,
    "naranja": 0.80,
    "uva": 2.00,
    "fresa": 3.00
}

# Solicitar al usuario un nombre de una fruta
fruta = input("Ingrese el nombre de una fruta: ").lower()

# Validar si la fruta existe en el diccionario
if fruta in diccionarioFrutas:
    # Si existe, preguntar la cantidad que desea comprar
    cantidad = int(input(f"¿Cuántas {fruta}s desea comprar? "))
    
    # Calcular el precio total
    precio_total = diccionarioFrutas[fruta] * cantidad
    
    # Mostrar el precio total
    print(f"El precio total por {cantidad} {fruta}(s) es: ${precio_total:.2f}")
else:
    # Si no existe, mostrar un mensaje correspondiente
    print("Lo siento, esa fruta no está disponible.")
