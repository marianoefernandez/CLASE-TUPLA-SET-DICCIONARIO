from salidas import *
from cargas import *

#Un diccionario es una coleccion que me permite guardar un conjunto de elementos representados por una clave y un valor, a diferencia de un array no tengo posiciones o indices tengo una clave entonces su acceso es mucho más intuitivo para representar datos concretos --> Por ejemplo la información de un alumno

#1.Declaración --> HAY VARIAS FORMAS DE CREAR UN DICCIONARIO

#FORMA A --> La verdad yo no la uso, es la menos intuitiva y es utilizando la palabra reservada dict()

#Representar un alumno --> Legajo, Nombre, Apellido, DNI , Edad y Nota Final

# alumno = dict([
#     ("legajo",11111),
#     ("nombre","Mariano"),
#     ("apellido","Fernandez"),
#     ("dni",44444444),
#     ("edad",44),
#     ("nota_final",8)
# ])

#FORMA B --> La más utilizada y es utilizando las llaves {}

# alumno = {
#     "legajo":11111,
#     "nombre":"Mariano",
#     "apellido":"Fernandez",
#     "dni":44444444,
#     "edad":44,
#     "nota_final":8
# }

#FORMA C --> Crear un diccionario vacio y empezar a llenarlo con datos linea por linea

# alumno = {}
# alumno["legajo"] = 11111
# alumno["nombre"] = "Mariano"
# alumno["apellido"] = "Fernandez"
# alumno["dni"] = 44444444
# alumno["edad"] = 44
# alumno["nota_final"] = 8

# print(alumno)

#2.Acceso

# alumno = {
#     "legajo":11111,
#     "nombre":"Mariano",
#     "apellido":"Fernandez",
#     "dni":44444444,
#     "edad":44,
#     "nota_final":8
# }

#MOSTRAR PARTE DEL DICCIONARIO (Tengo dos formas) 

#a)Utilizar los corchetes para acceder a la clave

#Quiero mostrar el apellido y la nota del alumno
# print(f"APELLIDO : {alumno["apellido"]}")
# print(f"NOTA FINAL : {alumno["nota_final"]}/10")
# print(f"GENERO : {alumno["genero"]}")

# #b)Utilizar el metodo get para evitar problemas...
# print(f"APELLIDO : {alumno.get("apellido")}")
# print(f"NOTA FINAL : {alumno.get("nota_final")}")
# # print(f"GENERO : {alumno.get("genero")}")#SI UTILIZO GET Y EL DATO NO LO ENCUENTRA, DEVUELVE NONE
# print(f"GENERO : {alumno.get("genero","No se encontro el dato")}")

#MUESTRO TODO EL DICCIONARIO
#print(alumno)
# #Tengo que crear mi propia funcion para mostrar el diccionario
# mostrar_diccionario_alumno(alumno)
# mostrar_diccionario(alumno,"ERROR. El alumno no se puede mostrar")

#3.Modificación
# alumno = {
#     "legajo":11111,
#     "nombre":"Mariano",
#     "apellido":"Fernandez",
#     "dni":44444444,
#     "edad":44,
#     "nota_final":8
# }

#Yo puedo modificar o agregar nuevos elementos al diccionario utilizando los corchetes o el metodo update.

#a)Cambiarle el apellido, la edad y la nota al alumno

#ALUMNO ANTES
# print("ALUMNO ANTES")
# mostrar_diccionario_alumno(alumno)

#FORMA A --> Utilizando los corchetes
# alumno["apellido"] = "Gomez"
# alumno["edad"] = 33
# alumno["nota_final"] = 7

#FORMA B --> El metodo update
# alumno.update({"apellido":"Gomez","edad":33,"nota_final":7})

# print("ALUMNO DESPUES")
# mostrar_diccionario_alumno(alumno)

#Agregar nueva información al diccionario
# alumno = {
#     "legajo":11111,
#     "nombre":"Mariano",
#     "apellido":"Fernandez",
#     "dni":44444444,
#     "edad":44,
#     "nota_final":8
# }

# print("ALUMNO ANTES")
# mostrar_diccionario(alumno)

#Quiero agregarle 
#Genero
#Domicilio
#Cantidad de materias aprobadas

# #FORMA A --> Utilizando los corchetes
# alumno["genero"] = "Masculino"
# alumno["domicilio"] = "Av Mitre 750"
# alumno["cantidad_materias_aprobadas"] = 8

# # print("ALUMNO DESPUES")
# # mostrar_diccionario(alumno)

# #FORMA B --> El metodo update
# alumno.update({"genero":"Masculino","domicilio":"Av Mitre 750","cantidad_materias_aprobadas":8})

# print("ALUMNO DESPUES")
# mostrar_diccionario(alumno)

#4.Carga

# alumno = {}
# print(f"ANTES DE LA CARGA --> {alumno}")
# cargar_alumno(alumno)
# print("DESPUES DE LA CARGA")
# mostrar_diccionario_alumno(alumno)

#5.Borrado

alumno = {
    "legajo":11111,
    "nombre":"Mariano",
    "apellido":"Fernandez",
    "dni":44444444,
    "edad":44,
    "nota_final":8
}

print("DICCIONARIO ANTES")
mostrar_diccionario(alumno)

#DEL --> PROBLEMA POSIBLE, SI LA CLAVE NO EXISTE DA ERROR
# del alumno["legajo"]
# del alumno["apellido"]

#POP --> POP DEVUELVE EL ELEMENTO ELIMINADO
#FORMA A --> Rompe si el elemento no existe
# alumno.pop("legajo")
# elemento_eliminado = alumno.pop("apellido")
# alumno.pop("apellido")#ROMPE

#FORMA B de usar el pop y es con una de sus sobrecargas
#Esta sobrecarga me permite devolver un valor por defecto en caso de que el elemento que quiso borrar no existe, EVITANDO QUE EL PROGRAMA ROMPA
# elemento_eliminado = alumno.pop("lalala","ERROR")
# print(f"Elemento eliminado --> {elemento_eliminado}")

# print("DICCIONARIO DESPUES")
# mostrar_diccionario(alumno)
# print(f"Apellido eliminado --> {elemento_eliminado}")
