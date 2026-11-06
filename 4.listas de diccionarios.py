from funciones import *
from salidas import *
from entradas import *
from cargas import *

#Crear una lista de diccionarios para guardar un alumno de una universidad

#nombre --> str
#apellido --> str
#legajo --> int (NO SE CARGAN, se genere de forma random)
#edad --> int
#nota_final --> int 

# lista_alumnos = [
#     {"nombre": "Juan", "apellido": "Pérez", "legajo": 48213, "edad": 19, "nota_final": 7},
#     {"nombre": "María", "apellido": "González", "legajo": 15729, "edad": 21, "nota_final": 9},
#     {"nombre": "Lucas", "apellido": "Rodríguez", "legajo": 93804, "edad": 20, "nota_final": 4},
#     {"nombre": "Sofía", "apellido": "Fernández", "legajo": 27461, "edad": 22, "nota_final": 8},
#     {"nombre": "Mateo", "apellido": "López", "legajo": 61058, "edad": 18, "nota_final": 6},
#     {"nombre": "Valentina", "apellido": "Martínez", "legajo": 34197, "edad": 23, "nota_final": 10},
#     {"nombre": "Tomás", "apellido": "Sánchez", "legajo": 82635, "edad": 25, "nota_final": 2},
#     {"nombre": "Camila", "apellido": "Romero", "legajo": 50942, "edad": 19, "nota_final": 7},
#     {"nombre": "Facundo", "apellido": "Díaz", "legajo": 19386, "edad": 27, "nota_final": 5},
#     {"nombre": "Martina", "apellido": "Álvarez", "legajo": 76520, "edad": 20, "nota_final": 8},
#     {"nombre": "Santiago", "apellido": "Torres", "legajo": 43871, "edad": 21, "nota_final": 3},
#     {"nombre": "Julieta", "apellido": "Ruiz", "legajo": 88014, "edad": 24, "nota_final": 9},
#     {"nombre": "Nicolás", "apellido": "Ramírez", "legajo": 25693, "edad": 22, "nota_final": 6},
#     {"nombre": "Agustina", "apellido": "Flores", "legajo": 67248, "edad": 18, "nota_final": 7},
#     {"nombre": "Joaquín", "apellido": "Acosta", "legajo": 31507, "edad": 30, "nota_final": 4},
#     {"nombre": "Lucía", "apellido": "Benítez", "legajo": 94362, "edad": 19, "nota_final": 10},
#     {"nombre": "Franco", "apellido": "Medina", "legajo": 12875, "edad": 26, "nota_final": 1},
#     {"nombre": "Florencia", "apellido": "Herrera", "legajo": 59430, "edad": 21, "nota_final": 8},
#     {"nombre": "Ignacio", "apellido": "Suárez", "legajo": 70186, "edad": 23, "nota_final": 5},
#     {"nombre": "Micaela", "apellido": "Castro", "legajo": 36659, "edad": 20, "nota_final": 6},
# ]

#lista_alumnos = []

#1.Cargar Alumnos --> Ya no se cargan 5 Elementos en el vector, 10 elementos, 20, etc, se carga de a uno
#2.Mostrar Alumnos --> FORMATO A ELECCION
#Mostrar que sucede si no se normalizan los datos.
# mostrar_lista_alumnos(lista_alumnos)

#TAREA PARA CASA

#3.Mostrar alumnos entre 18 y 30 años --> MISMA FUNCION
#4.Mostrar alumnos promocionados (6 y 10) --> MISMA FUNCION
#5.Mostrar alumnos regularizados (4 y 5) --> MISMA FUNCION
#6.Mostrar alumnos que recursaron (1 y 3) --> MISMA FUNCION
#7.Porcentaje de alumnos promocionados - regularizados - recursados
#8.Ordenar alfabeticamentamente a los alumnos (Hay que normalizar los datos)
#9.Mostrar los apellidos de todos los alumnos sin repetir, además mostrar cuantos alumnos tienen el mismo apellido.
#Por ejemplo 
#Fernández = 7
#Gomez = 5
#Etc...

#ESTO DESPUES ENCARGUENSE DE LLEVARLO A menu.py
lista_alumnos = []
seguir = True

while seguir:
    print("\n========== MENÚ ==========")
    print("1. Cargar alumno")
    print("2. Mostrar alumnos")
    print("3. Mostrar alumnos entre 18 y 30 años")
    print("4. Mostrar alumnos promocionados (6 a 10)")
    print("5. Mostrar alumnos regularizados (4 y 5)")
    print("6. Mostrar alumnos que recursan (1 a 3)")
    print("7. Porcentaje de promocionados, regularizados y recursantes")
    print("8. Ordenar alumnos alfabéticamente")
    print("9. Mostrar apellidos sin repetir y cuántos alumnos tienen cada uno")
    print("0. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        cargar_alumno_lista(lista_alumnos)
        pass
    elif opcion == "2":
       mostrar_lista_alumnos(lista_alumnos)
    elif opcion == "3":
        pass  # mostrar_alumnos_por_rango(lista_alumnos, "edad", 18, 30)
    elif opcion == "4":
        pass  # mostrar_alumnos_por_rango(lista_alumnos, "nota_final", 6, 10)
    elif opcion == "5":
        pass  # mostrar_alumnos_por_rango(lista_alumnos, "nota_final", 4, 5)
    elif opcion == "6":
        pass  # mostrar_alumnos_por_rango(lista_alumnos, "nota_final", 1, 3)
    elif opcion == "7":
        pass  # mostrar_porcentajes(lista_alumnos)
    elif opcion == "8":
        pass  # ordenar_alumnos(lista_alumnos)
    elif opcion == "9":
        pass  # mostrar_apellidos(lista_alumnos)
    elif opcion == "0":
        seguir = False
        print("Saliendo...")
    else:
        print("Opción inválida.")