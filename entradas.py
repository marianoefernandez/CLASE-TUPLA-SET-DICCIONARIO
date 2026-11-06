from funciones import verificar_es_entero, reemplazar_caracteres, contar_letras, eliminar_espacios,verificar_es_nombre_propio

def ingresar_cadena(mensaje:str, mensaje_error:str = "ERROR, la cadena no puede estar vacia",cantidad_minima:int = 1):
    cadena = input(mensaje)

    while len(cadena) < cantidad_minima:
        print(mensaje_error)
        cadena = input(mensaje)

    return cadena


def ingresar_entero_positivo(mensaje:str = "Ingrese un numero: ",mensaje_error_1:str = "ERROR, el numero no puede estar vacio ", mensaje_error_2:str = "El numero es negativo o esta en un formato invalido") -> int:
    numero_str = ingresar_cadena(mensaje,mensaje_error_1)
    numero_str = reemplazar_caracteres(numero_str," ","")

    while not verificar_es_entero(numero_str):
        print(mensaje_error_2)
        numero_str = ingresar_cadena(mensaje,mensaje_error_1)
        numero_str = reemplazar_caracteres(numero_str," ","")

    numero = int(numero_str)

    return numero

# def ingresar_entero_rango(minimo:int,maximo:int,mensaje:str = "Ingrese un numero: ",mensaje_error_1:str = "ERROR, el numero no puede estar vacio ", mensaje_error_2:str = "El numero es negativo o esta en un formato invalido",mensaje_error_3:str = "Rango invalido") -> int:
#     numero = ingresar_entero_positivo(mensaje,mensaje_error_1,mensaje_error_2)

#     while numero > maximo or numero < minimo:
#         print(mensaje_error_3)
#         numero = ingresar_entero_positivo(mensaje,mensaje_error_1,mensaje_error_2)

#     return numero

def ingresar_entero_rango(rango:tuple,mensaje:str = "Ingrese un numero: ", mensajes_error: tuple = ("ERROR, el numero no puede estar vacio", "ERROR, el numero es invalido","ERROR, el numero esta fuera de rango") ) -> int:
    mensaje_error_1,mensaje_error_2,mensaje_error_3 = mensajes_error
    minimo,maximo = rango
    numero = ingresar_entero_positivo(mensaje,mensaje_error_1,mensaje_error_2)

    while numero > maximo or numero < minimo:
        print(mensaje_error_3)
        numero = ingresar_entero_positivo(mensaje,mensaje_error_1,mensaje_error_2)

    return numero

def ingresar_cadena_letras(mensaje:str, mensaje_error:str = "ERROR, la cadena no puede no tener letras",cantidad_minima:int = 1):
    cadena = input(mensaje)

    while contar_letras(cadena) < cantidad_minima:
        print(mensaje_error)
        cadena = input(mensaje)

    return cadena

def ingresar_nombre_propio(mensaje:str, mensaje_error_1:str = "ERROR, la cadena no puede tener menos de 3 letras",mensaje_error_2:str = "La cadena tiene que tener solo letras",cantidad_minima:int = 3):
    #Me va a servir para ingresar un nombre o un apellido.
    nombre_propio = ingresar_cadena_letras(mensaje,mensaje_error_1,cantidad_minima)
    nombre_propio = eliminar_espacios(nombre_propio)

    while not verificar_es_nombre_propio(nombre_propio):
        print(mensaje_error_2)
        nombre_propio = ingresar_cadena_letras(mensaje,mensaje_error_1)

    return nombre_propio
    #Recomendacion --> Normalizar el nombre
    # return convertir_titulo(nombre_propio)#mARIANo ezEQUIEL --> Mariano Ezequiel
