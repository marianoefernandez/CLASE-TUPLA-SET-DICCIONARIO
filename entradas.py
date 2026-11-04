from funciones import verificar_es_entero, reemplazar_caracteres

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

