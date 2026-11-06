from configuraciones import ASC , DESC

def reemplazar_caracteres(cadena_original:str,caracter_reemplazar:str,reemplazo:str) -> str:
    cadena_copia = ""
    
    for i in range(len(cadena_original)):
        if cadena_original[i] == caracter_reemplazar:
            cadena_copia += reemplazo
        else:
            cadena_copia += cadena_original[i]

    return cadena_copia

def eliminar_espacios(cadena_original:str):
    cadena_copia = ""
    
    for i in range(len(cadena_original)):
        if cadena_original[i] == " " and (i == 0 or cadena_original[i - 1] == " "):
            cadena_copia += ""
        else:
            cadena_copia += cadena_original[i]

    if cadena_copia[-1] == " ":#Si el último caracter es un espacio
        cadena_copia = cadena_copia[:-1]#Me elimina el último caracter

    return cadena_copia

def contar_letras(cadena:str) -> int:
    contador = 0

    if verificar_cadena(cadena):
        cadena = convertir_minuscula(cadena)#Normalizar
        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if verificar_minuscula(caracter_ascii):
                contador += 1

    return contador

def verificar_es_entero(cadena:str) -> bool:
    if verificar_cadena(cadena):
        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if not verificar_numero(caracter_ascii):
                return False

        return True
    else:
        return False

def verificar_numero(caracter_ascii:int) -> bool:
    return caracter_ascii >= 48 and caracter_ascii <= 57

def verificar_cadena(cadena:str) -> bool:
    return type(cadena) == str and len(cadena) > 0

def verificar_array(array:list) -> bool:
    return type(array) == list and len(array) > 0

def eliminar_repeticiones(lista:list) -> list:
    if verificar_array(lista):
        conjunto = set()
        conjunto.update(lista)#Elimina las repeticiones
        lista_sin_repeticion = list(conjunto)
        return lista_sin_repeticion
    else:
        return []

def contar_dato(lista:list,dato:any) -> int | None:
    #Cuenta la cantidad de veces que ese dato se encuentra en la lista
    contador = 0
    if type(lista) == list:
        for i in range(len(lista)):
            if dato == lista[i]:
                contador += 1
        return contador
    
    return None

def verificar_array_cadenas(array:list) -> bool:
    if verificar_array(array):
        for i in range(len(array)):
            if not verificar_cadena(array[i]):
                return False

        return True
    else:
        return False

def ordenar_array_caracteres(lista_caracteres:list,criterio:bool = ASC):
    if verificar_array_cadenas(lista_caracteres):
        for izq in range(len(lista_caracteres) - 1):
            for der in range(izq + 1,len(lista_caracteres)):
                if criterio == ASC and lista_caracteres[izq] > lista_caracteres[der]:
                    intercambiar_array(lista_caracteres,izq,der)
                elif criterio == DESC and lista_caracteres[izq] < lista_caracteres[der]:
                    intercambiar_array(lista_caracteres,izq,der)
        return True
    else:
        return False

def intercambiar_array(lista:list,izq:int,der:int) -> None:
    aux_izq = lista[izq]
    lista[izq] = lista[der]
    lista[der] = aux_izq

def crear_conjunto_lista(lista:list) -> set: 
    conjunto = set()
    if verificar_array(lista):
        conjunto.update(lista)
    
    return conjunto

def calcular_intercepcion_listas(lista_uno:list,lista_dos:list) -> list:
    conjunto_uno = crear_conjunto_lista(lista_uno)
    conjunto_dos = crear_conjunto_lista(lista_dos)
    conjunto_final = conjunto_uno.intersection(conjunto_dos)
    lista_resultado = list(conjunto_final)
    return lista_resultado

def convertir_minuscula(cadena_original:str) -> str:   
    cadena_copia = ""

    for i in range(len(cadena_original)):
        caracter_original = cadena_original[i]
        caracter_ascii = ord(caracter_original)
        if verificar_mayuscula(caracter_ascii):#Si es mayuscula
            caracter_minuscula = chr(caracter_ascii + 32)
            cadena_copia += caracter_minuscula
        else:
            cadena_copia += caracter_original

    return cadena_copia

def convertir_mayuscula(cadena_original:str) -> str:
    cadena_copia = ""

    for i in range(len(cadena_original)):
        caracter_original = cadena_original[i]
        caracter_ascii = ord(caracter_original)
        if verificar_minuscula(caracter_ascii):#Si es mayuscula
            caracter_minuscula = chr(caracter_ascii - 32)
            cadena_copia += caracter_minuscula
        else:
            cadena_copia += caracter_original

    return cadena_copia

def convertir_titulo(cadena_original:str) -> str:
    cadena_original = convertir_minuscula(cadena_original) 
    cadena_original = eliminar_espacios(cadena_original)
    cadena_copia = ""

    for i in range(len(cadena_original)):
        if i == 0 or cadena_original[i - 1] == " ":
            cadena_copia += convertir_mayuscula(cadena_original[i]) 
        else:
            cadena_copia += cadena_original[i]

    return cadena_copia

def normalizar_minuscula(lista_caracteres:list) -> bool:
    if verificar_array_cadenas(lista_caracteres):
        for i in range(len(lista_caracteres)):
            lista_caracteres[i] = eliminar_espacios(lista_caracteres[i])
            lista_caracteres[i] = convertir_minuscula(lista_caracteres[i])
        return True
    else:
        return False

def normalizar_nombre(lista_caracteres:list) -> bool:
    if verificar_array_cadenas(lista_caracteres):
        for i in range(len(lista_caracteres)):
            lista_caracteres[i] = eliminar_espacios(lista_caracteres[i])
            lista_caracteres[i] = convertir_titulo(lista_caracteres[i])
        return True
    else:
        return False

def verificar_mayuscula(caracter_ascii:int) -> bool:
    return (caracter_ascii >= 65 and caracter_ascii <= 90) or caracter_ascii == 209

def verificar_cadena(cadena:str) -> bool:
    return type(cadena) == str and len(cadena) > 0

def verificar_minuscula(caracter_ascii:int) -> bool:
    return (caracter_ascii >= 97 and caracter_ascii <= 122) or caracter_ascii == 241

def verificar_es_nombre_propio(cadena:str) -> bool:
    if verificar_cadena(cadena):
        cadena = convertir_minuscula(cadena)#Normalizar (llevar la cadena a un solo formato)

        for i in range(len(cadena)):
            caracter_ascii = ord(cadena[i])
            if not verificar_minuscula(caracter_ascii) and caracter_ascii != 32:
                return False

        return True
    else:
        return False

def formatear_clave(clave:str) -> str:
    pass

