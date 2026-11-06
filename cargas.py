import random
from entradas import *
from funciones import verificar_array
from salidas import mostrar_diccionario_alumno
from configuraciones import RANGO_EDAD, MENSAJE_ERROR_EDAD, RANGO_DNI, MENSAJE_ERROR_DNI, RANGO_NOTA,MENSAJE_ERROR_NOTA

def cargar_alumno(alumno:dict) -> bool:
    if type(alumno) == dict:
        #Pedimos todos los datos
        #El legajo se genere random
        alumno["legajo"] = random.randint(11111,99999)
        alumno["nombre"] = ingresar_nombre_propio("Ingrese su nombre: ","Error, el nombre no puede tener menos de 3 caracteres","Error, el nombre debe tener solo letras")
        alumno["apellido"] = ingresar_nombre_propio("Ingrese su apellido: ","Error, el apellido no puede tener menos de 3 caracteres","Error, el apellido debe tener solo letras")
        alumno["edad"] = ingresar_entero_rango(RANGO_EDAD,"Ingrese su edad: ",MENSAJE_ERROR_EDAD)
        alumno["dni"]  = ingresar_entero_rango(RANGO_DNI,"Ingrese su dni: ",MENSAJE_ERROR_DNI)
        alumno["nota_final"] = ingresar_entero_rango(RANGO_NOTA,"Ingrese su nota: ",MENSAJE_ERROR_NOTA)
        return True
    else:
        return False

def cargar_alumno_lista(lista_alumnos:list) -> bool:
    if type(lista_alumnos) == list:
        print("CARGANDO ALUMNO\n")
        alumno = {}
        cargar_alumno(alumno)
        mostrar_diccionario_alumno(alumno)
        respuesta = input("¿Desea realmente cargar a este alumno? si/no")#Mejoren, creen su propia funcion para pedir una respuesta

        if respuesta == "si":
            lista_alumnos.append(alumno)
            print("CARGA REALIZADA CON EXITO")
            return True
        else:
            print(f"El usuario cancelo la carga")
            return False
    else:
        return False
    