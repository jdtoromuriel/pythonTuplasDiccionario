#Tuplas

"""
tupla1= ()
tupla2= (1, "texto", 1.0, True)
Son inmutables
Son indezadas
metodos no compatibles con las tuplas: insert, del?, append, sort
"""

dias_semana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")

print(type(dias_semana))

print(dias_semana[3])

print(dias_semana.index("Miercoles"))
# dias_semana["Lunes"] = "Sabado"
print(dias_semana)

print(dias_semana.count("Lunes"))
# # Convertir una tupla en lista
# lista_dias = list(dias_semana)

# print(lista_dias)
# #Eliminar objeto dias_Semana

del dias_semana

print(dias_semana)