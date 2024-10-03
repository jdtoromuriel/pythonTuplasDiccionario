# Diccionario

datos_personales = {"nombre": "Cristian", "apellidos": "Perez", "edad": 22, "Sexo": "M"}

print(type(datos_personales))
# # Opcion 2
# datos = dict(nombre="Cristian", apellidos="Perez", edad=22, sexo="M")

# print(type(datos))
print(datos_personales["edad"])
print(datos_personales.get("edad"))

#Modificar edad de karina
datos_personales["edad"] = 23
print(datos_personales.get("edad"))
datos_personales["Fecha_nac"] = "01/01/1990"

print(datos_personales)
# Eliminar elemento
#Pop(clave)
#popitem()
# datos_personales.pop("Fecha_nac")
# datos_personales.popitem()
# print(datos_personales)
#del, clear


#key(), value(), items()
claves = datos_personales.keys()
print(claves)

for c in datos_personales.keys():
    print(c)

#Values; Obtiene losdatos del diccionario
valores = datos_personales.values()
print(valores)

for v in datos_personales.values():
    print(v)

#Items; Obtiene clave y valores al tiempo
items = datos_personales.items()
print(items)

for c,v in datos_personales.items():
    print(f"Item: {c} | Clave: {v}")

otros_datos = {
    "Fecha_nac": "01/01/1990",
    "profesion": "Ingeniero",
    "ocupacion": "Docente"
}
#Update: actualizar el diccionario
datos_personales.update(otros_datos)
print(datos_personales)
