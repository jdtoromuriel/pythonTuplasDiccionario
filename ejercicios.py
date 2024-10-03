#EJERCICIO 1
# SOLICITAR UN NUMERO POR TECLADO Y CREAR UN DICCIONARIO, CUYAS CLAVES SEAN DESDE EL 1 HASTA
# EL NUMERO INGRESADO Y LOS VALORES SEAN EL CUBO DE LAS CLAVES. MOSTRAR CLAVES Y SU VALOR
# CORRESPONDIENTE

numDiccionario = int(input("Ingrese un numero: "))

diccionario = {i: i**3 for i in range(1, numDiccionario + 1)}

for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")
print(diccionario)
#EJERCICIO 2
# crear un diccionario que almacene nombres de fruta como clave y su precio
# como valor solicitar al usuario un nombre de una fruta (validar si la fruta existe o no) si no 
# existe mostrar el mensaje correspondiente, si existe preguntar la cantidad que desea comprar y debe 
# mostra cual seria el precio total

frutas = {
    "pera": 1000,
    "kiwi": 5000,
    "banano": 700,
    "manzana": 3000,
}

print("Lista de frutas que vendemos:")
print(frutas)
fruta = input("Ingrese una fruta: ").lower()

if fruta in frutas:
    cantidad = int(input(f"¿Cuantas {fruta}s desea comprar? "))
    precioTotal = frutas[fruta] * cantidad

    print(f"El precio total es: ${precioTotal}")
else:
    print("No tenemos esa fruta")