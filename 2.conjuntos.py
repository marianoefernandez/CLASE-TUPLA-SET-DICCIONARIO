from funciones import *

#Los conjuntos son una colección (como las listas,tuplas,diccionarios) pero estas mismas tienen las siguientes caracteristicas
#1.Sus elementos son unicos (NO SE PUEDEN REPETIR)
#2.El orden del mismo es 'raro'
#3.Los elementos son mutables 
#4.Los conjuntos NO SON INDEXABLES (No tienen indice)

#Como creo un conjunto

#Para crear un conjunto yo uso las llaves {}, pero tambien para crear diccionario (que pronto vamos a verlo) tambien uso las llaves por lo que puede gener un par de conflictos.

#Creando mi primer conjunto
# conjunto = {3,5,9,5,3,4,3}#Orden raro, tiene en cuenta el hash de cada numero
# print(type(conjunto))
# print(f"Conjunto --> {conjunto}")

#Creando un conjunto vacio
# conjunto = {}
# print(type(conjunto))
# print(f"Conjunto --> {conjunto}")
#Si la {} esta vacia no me crea un conjunto, me crea un diccionario que es otro tipo de coleccion

#Para poder crear un conjunto vacio utilizo la palabra reservada set()
# conjunto = set()
# print(type(conjunto))
# print(f"Conjunto --> {conjunto}")

#Un conjunto es un objeto mutable por lo que puedo modificarlo a mi gusto utilizando sus propios metodos (add,remove, discard)

#1)AGREGAR ELEMENTO A UN CONJUNTO
#Solo se pueden agregar elementos que no existan en el conjunto, si el elemento ya existia no lo agrega

# conjunto = {3,5,9,5,3,4,3}
# print(f"Conjunto antes --> {conjunto}")
# # conjunto.add(100)#LO AGREGA
# # conjunto.add(9)#NO LO AGREGA
# print(f"Conjunto despues --> {conjunto}")

#2.ELIMINAR ELEMENTOS (REMOVE, DISCARD y POP)
# conjunto = {3,5,9,5,3,4,3}
# print(f"Conjunto antes --> {conjunto}")

#Remove --> Elimina el elemento del set, si este no existe lanza un error.
# conjunto.remove(9)
# conjunto.remove(100)#Lanza un error si el elemento que quiero borrar no existe

#Discard --> Elimina el elemento del set, pero no hace nada en caso de que el elemento no exista

# conjunto.discard(9)
# conjunto.discard(100)#Ahora con el discard no rompe

#Pop --> Elimina el primer elemento del conjunto y lo devuelve, si el conjunto esta vacio el pop() tira un error.
# elemento_eliminado = conjunto.pop()
# print(f"Elemento eliminado : {elemento_eliminado}")
# print(f"Conjunto despues --> {conjunto}")

# for i in range(5):
#     elemento_eliminado = conjunto.pop()
#     print(f"Elemento eliminado : {elemento_eliminado}")
#     print(f"Conjunto despues --> {conjunto}")

#Para limpiar el set utilizamos clear

# conjunto = {3,5,9,5,3,4,3}
# print(f"Conjunto antes --> {conjunto}")
# conjunto.clear()
# print(f"Conjunto despues --> {conjunto}")

#3.METODOS EXTRA --> union, interception,update, vemos el operador (-)

#a)UNION

# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}
# conjunto_resultado = conjunto_a.union(conjunto_b) # a U b

# print(f"a = {conjunto_a}")
# print(f"b = {conjunto_b}")
# print(f"a U b = {conjunto_resultado}")

#b)INTERCEPCION
# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}
# conjunto_resultado = conjunto_a.intersection(conjunto_b) # a ∩ b

# print(f"a = {conjunto_a}")
# print(f"b = {conjunto_b}")
# if len(conjunto_resultado) > 0:
#     print(f"a ∩ b = {conjunto_resultado}")
# else:
#     print("a ∩ b = {}")

#c)DIFERENCIA

#a - b

# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}
# conjunto_resultado = conjunto_a.difference(conjunto_b)#FORMA A
# conjunto_resultado = conjunto_a - conjunto_b#FORMA B

# print(f"a = {conjunto_a}")
# print(f"b = {conjunto_b}")
# if len(conjunto_resultado) > 0:
#     print(f"a - b = {conjunto_resultado}")
# else:
#     print("a - b = {}")

# #b - a
# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}
# conjunto_resultado = conjunto_b.difference(conjunto_a)#FORMA A
# conjunto_resultado = conjunto_b - conjunto_a#FORMA B

# print(f"a = {conjunto_a}")
# print(f"b = {conjunto_b}")
# if len(conjunto_resultado) > 0:
#     print(f"b - a = {conjunto_resultado}")
# else:
#     print("b - a = {}")

#d) UPDATE
# conjunto_a = {1,2,3}
# conjunto_b = {3,4,5}

# print(f"Conjunto a antes = {conjunto_a}")
# conjunto_a.update(conjunto_b)
# print(f"Conjunto a antes = {conjunto_a}")

#YO PUEDO CON EL UPDATE UNIR UNA LISTA, UNA TUPLA o LO QUE QUIERA A UN CONJUNTO

# nombres = [
#     "Sebastián", "Valentina", "Lucía", "Florencia", "Natalia",
#     "Florencia", "Natalia", "Benjamín", "Franco", "Florencia",
#     "Lucía", "Camila", "Emilio", "Camila", "Martina",
#     "Ignacio", "Ignacio", "Camila", "Emma", "Sofía",
#     "Valeria", "Isabella", "Natalia", "Mateo", "Martina",
#     "Valentina", "Martina", "Renata", "Facundo", "Benjamín",
#     "Natalia", "Sebastián", "Tomás", "Valentina", "Franco",
#     "Camila", "Franco", "Lucía", "Natalia", "Daniela",
#     "Lucía", "Valentina", "Emma", "Franco", "Agustina",
#     "Ramiro", "Facundo", "Emma", "Agustín", "Nicolás"
# ]

# #Yo puedo con el update copiar una lista en un set 
# conjunto_nombres = set()
# print(f"CONJUNTO ANTES: {conjunto_nombres}")
# conjunto_nombres.update(nombres)
# print(f"CONJUNTO DESPUES: {conjunto_nombres}")

#LOS CONJUNTOS NO SON INDEXABLES (NO TIENEN INDICE O POSICION)

# conjunto = {3,5,9,5,3,4,3}
# print(conjunto)
# # print(conjunto[0])#LOS CONJUNTOS NO TIENEN POSICION/INDICE

# #ESTO NO SIGNIFICA QUE NO PUEDA RECORRER UN CONJUNTO EN UN FOR, PERO NO CON FOR I IN RANGE(), VOY A TENER QUE USAR EL OTRO FOR.

# for elemento in conjunto:
#     if elemento % 2 == 0:
#         print(elemento)


#region ¿PARA QUE LOS VAMOS A USAR?

#¿PARA QUE LOS VAMOS A USAR?

nombres = [
    "Sebastián", "Valentina", "Lucía", "Florencia", "Natalia",
    "Florencia", "Natalia", "Benjamín", "Franco", "Florencia",
    "Lucía", "Camila", "Emilio", "Camila", "Martina",
    "Ignacio", "Ignacio", "Camila", "Emma", "Sofía",
    "Valeria", "Isabella", "Natalia", "Mateo", "Martina",
    "Valentina", "Martina", "Renata", "Facundo", "Benjamín",
    "Natalia", "Sebastián", "Tomás", "Valentina", "Franco",
    "Camila", "Franco", "Lucía", "Natalia", "Daniela",
    "Lucía", "Valentina", "Emma", "Franco", "Agustina",
    "Ramiro", "Facundo", "Emma", "Agustín", "Nicolás"
]

nombres_2 = [
    "Abril", "Milagros", "Julieta", "Sofía", "Antonella",
    "Catalina", "Constanza", "Valentina", "Guadalupe", "Macarena",
    "Aldana", "Brenda", "Micaela", "Camila", "Rocío",
    "Ayelén", "Belén", "Carla", "Eugenia", "Gisel",
    "Noelia", "Paola", "Lucía", "Vanesa", "Emma",
    "Alexis", "Braian", "Cristian", "Diego", "Santiago",
    "Esteban", "Fernando", "Gonzalo", "Hernán", "Mateo",
    "Iván", "Javier", "Kevin", "Leonardo", "Marcos",
    "Nahuel", "Tomás", "Osvaldo", "Pablo", "Rodrigo",
    "Sergio", "Tobias", "Ulises", "Lucas", "Agustina"
]

#1)Mostrar los nombres sin repetir

#2)Mostrar cuantas veces se repite cada nombre

#3)Mostrar los nombres que repiten tanto en la lista 1 como en la lista 2

#endregion